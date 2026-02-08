import re
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from datetime import datetime


def create_header_footer(canvas, doc):

    canvas.saveState()
    footer_text = " Content Calendar | Omar Elgema3y"
    canvas.setFont('Helvetica', 9)
    canvas.setFillColor(colors.HexColor('#718096'))
    canvas.drawCentredString(letter[0] / 2, 0.5 * inch, footer_text)
    page_num = f"Page {doc.page}"
    canvas.drawRightString(letter[0] - 0.75 * inch, 0.5 * inch, page_num)
    canvas.restoreState()


def parse_text_output(text):
    """Parse the text output from the AI agent"""
    data = {
        "brand_name": "Content Calendar",
        "month": datetime.now().strftime("%B %Y"),
        "stats": {"total_posts": 30, "platforms": 5, "posts_per_week": 7, "content_themes": 4},
        "content_pillars": [],
        "posts": [],
        "hashtag_bank": [],
        "posting_schedule": [],
        "kpi_targets": []
    }
    
    # Extract brand name
    brand_match = re.search(r'brand name:?\s*(.+?)(?:\n|$)', text, re.IGNORECASE)
    if brand_match:
        data["brand_name"] = brand_match.group(1).strip()
    
    # Extract content pillars
    pillar_section = re.search(r'CONTENT PILLARS?.*?:(.*?)(?:POSTS?:|SOCIAL MEDIA|$)', text, re.DOTALL | re.IGNORECASE)
    if pillar_section:
        pillar_text = pillar_section.group(1)
        pillar_matches = re.findall(r'(?:pillar|theme)\s*\d*[:\-]\s*(.+?)(?:\n|description)', pillar_text, re.IGNORECASE)
        for i, pillar in enumerate(pillar_matches[:6]):
            data["content_pillars"].append({
                "title": pillar.strip(),
                "description": f"Strategic content focused on {pillar.strip().lower()}"
            })
    
    # If no pillars found, add defaults
    if len(data["content_pillars"]) == 0:
        data["content_pillars"] = [
            {"title": "Brand Awareness", "description": "Build brand recognition and visibility"},
            {"title": "Engagement", "description": "Foster community interaction"},
            {"title": "Education", "description": "Share valuable insights"},
            {"title": "Promotion", "description": "Highlight products and services"}
        ]
    
    # Extract posts - look for numbered posts
    post_sections = re.findall(r'(?:post|#)\s*(\d+)[:\-\s]+(.*?)(?=(?:post|#)\s*\d+|hashtag bank|posting schedule|kpi|$)', text, re.DOTALL | re.IGNORECASE)
    
    platforms = ['instagram', 'linkedin', 'twitter', 'facebook', 'tiktok']
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    times = ['9:00 AM', '12:00 PM', '3:00 PM', '6:00 PM', '7:00 PM']
    content_types = ['Educational', 'Promotional', 'Entertaining', 'Inspirational', 'Behind-the-Scenes']
    
    for i, (num, content) in enumerate(post_sections[:35]):
        # Extract platform
        platform = 'instagram'
        for p in platforms:
            if p in content.lower():
                platform = p
                break
        
        # Extract title
        title_match = re.search(r'title[:\-]\s*(.+?)(?:\n|content)', content, re.IGNORECASE)
        title = title_match.group(1).strip() if title_match else f"Engaging {platform.title()} Post"
        
        # Extract content
        content_match = re.search(r'(?:content|caption|post)[:\-]\s*(.+?)(?:\n\n|hashtag|$)', content, re.DOTALL | re.IGNORECASE)
        post_content = content_match.group(1).strip() if content_match else content[:200].strip()
        
        # Extract hashtags
        hashtag_match = re.findall(r'#(\w+)', content)
        if not hashtag_match:
            hashtag_match = ['BrandName', 'Marketing', 'SocialMedia', 'Content', 'Digital']
        
        data["posts"].append({
            "post_number": int(num),
            "platform": platform,
            "title": title[:80],
            "content": post_content[:300] if len(post_content) > 50 else f"{post_content} Join us in our journey to create amazing content that resonates with our community.",
            "hashtags": hashtag_match[:8],
            "posting_day": days[i % 7],
            "posting_time": times[i % 5],
            "content_type": content_types[i % 5]
        })
    
    # If we didn't find enough posts, create them
    while len(data["posts"]) < 30:
        i = len(data["posts"])
        data["posts"].append({
            "post_number": i + 1,
            "platform": platforms[i % 5],
            "title": f"Engaging {platforms[i % 5].title()} Content",
            "content": f"Share valuable insights and connect with your audience through authentic storytelling. This post is designed to engage your followers and build lasting relationships with your community members.",
            "hashtags": ['Marketing', 'SocialMedia', 'Content', 'Digital', 'Brand'],
            "posting_day": days[i % 7],
            "posting_time": times[i % 5],
            "content_type": content_types[i % 5]
        })
    
    # Extract hashtags
    hashtag_section = re.search(r'HASHTAG BANK.*?:(.*?)(?:POSTING SCHEDULE|KPI|$)', text, re.DOTALL | re.IGNORECASE)
    if hashtag_section:
        data["hashtag_bank"] = re.findall(r'#?(\w+)', hashtag_section.group(1))[:30]
    
    if len(data["hashtag_bank"]) == 0:
        data["hashtag_bank"] = ['Marketing', 'SocialMedia', 'ContentCreation', 'DigitalMarketing', 'BrandAwareness',
                                 'Engagement', 'SocialMediaMarketing', 'ContentStrategy', 'OnlineMarketing', 'Business',
                                 'Entrepreneur', 'SmallBusiness', 'Branding', 'ContentMarketing', 'InboundMarketing']
    
    # Posting schedule
    data["posting_schedule"] = [
        {"platform": "Instagram", "frequency": "Daily", "best_times": "9 AM, 1 PM, 7 PM", "content_type": "Visual Stories"},
        {"platform": "LinkedIn", "frequency": "5x/week", "best_times": "8 AM, 12 PM, 5 PM", "content_type": "Professional Insights"},
        {"platform": "Twitter", "frequency": "Daily", "best_times": "9 AM, 3 PM, 8 PM", "content_type": "Quick Updates"},
        {"platform": "Facebook", "frequency": "4x/week", "best_times": "10 AM, 1 PM, 6 PM", "content_type": "Community Content"},
        {"platform": "TikTok", "frequency": "3x/week", "best_times": "6 PM, 8 PM, 10 PM", "content_type": "Trending Videos"}
    ]
    
    # KPI targets
    data["kpi_targets"] = [
        {"metric": "Engagement Rate", "target": "5.2%"},
        {"metric": "Follower Growth", "target": "+15%"},
        {"metric": "Reach", "target": "50K+"},
        {"metric": "Click-Through Rate", "target": "3.8%"},
        {"metric": "Shares", "target": "500+"},
        {"metric": "Comments", "target": "200+"},
        {"metric": "Saves", "target": "300+"},
        {"metric": "Video Views", "target": "25K+"}
    ]
    
    data["stats"]["total_posts"] = len(data["posts"])
    
    return data


def generate_pdf(result):
    """Generate a professional PDF content calendar"""
    
    # Parse the text output
    text = str(result.raw) if hasattr(result, 'raw') else str(result)
    data = parse_text_output(text)
    
    output_path = "Content_Calendar.pdf"
    
    doc = SimpleDocTemplate(output_path, pagesize=letter,
                           rightMargin=0.75*inch, leftMargin=0.75*inch,
                           topMargin=1*inch, bottomMargin=1*inch)
    
    elements = []
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle('CustomTitle', parent=styles['Heading1'],
                                 fontSize=28, textColor=colors.HexColor('#667eea'),
                                 spaceAfter=10, alignment=TA_CENTER, fontName='Helvetica-Bold')
    
    subtitle_style = ParagraphStyle('CustomSubtitle', parent=styles['Normal'],
                                    fontSize=14, textColor=colors.HexColor('#764ba2'),
                                    spaceAfter=30, alignment=TA_CENTER)
    
    section_header_style = ParagraphStyle('SectionHeader', parent=styles['Heading2'],
                                         fontSize=18, textColor=colors.HexColor('#667eea'),
                                         spaceAfter=15, spaceBefore=20, fontName='Helvetica-Bold')
    
    normal_style = ParagraphStyle('CustomNormal', parent=styles['Normal'],
                                 fontSize=10, textColor=colors.HexColor('#4a5568'), spaceAfter=12)
    
    # Title
    elements.append(Spacer(1, 1*inch))
    elements.append(Paragraph(data['brand_name'], title_style))
    elements.append(Paragraph(f"Content Calendar - {data['month']}", subtitle_style))
    elements.append(Spacer(1, 0.5*inch))
    
    # Stats table
    stats = data['stats']
    stats_data = [
        ['Total Posts', 'Platforms', 'Posts/Week', 'Content Themes'],
        [str(stats['total_posts']), str(stats['platforms']), str(stats['posts_per_week']), str(stats['content_themes'])]
    ]
    
    stats_table = Table(stats_data, colWidths=[1.5*inch]*4)
    stats_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#667eea')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,0), 12),
        ('BOTTOMPADDING', (0,0), (-1,0), 12),
        ('TOPPADDING', (0,0), (-1,0), 12),
        ('BACKGROUND', (0,1), (-1,-1), colors.HexColor('#f7fafc')),
        ('TEXTCOLOR', (0,1), (-1,-1), colors.HexColor('#667eea')),
        ('FONTNAME', (0,1), (-1,-1), 'Helvetica-Bold'),
        ('FONTSIZE', (0,1), (-1,-1), 20),
        ('TOPPADDING', (0,1), (-1,-1), 15),
        ('GRID', (0,0), (-1,-1), 1, colors.HexColor('#e2e8f0'))
    ]))
    
    elements.append(stats_table)
    elements.append(Spacer(1, 0.5*inch))
    
    # Content Pillars
    if data['content_pillars']:
        elements.append(Paragraph("Content Pillars", section_header_style))
        pillar_data = [['Pillar', 'Description']]
        for pillar in data['content_pillars']:
            pillar_data.append([pillar['title'], pillar['description']])
        
        pillar_table = Table(pillar_data, colWidths=[2*inch, 4.5*inch])
        pillar_table.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#764ba2')),
            ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
            ('ALIGN', (0,0), (-1,-1), 'LEFT'),
            ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
            ('FONTSIZE', (0,0), (-1,0), 11),
            ('BOTTOMPADDING', (0,0), (-1,0), 10),
            ('BACKGROUND', (0,1), (-1,-1), colors.HexColor('#f8f9fa')),
            ('GRID', (0,0), (-1,-1), 1, colors.HexColor('#e2e8f0')),
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
            ('TOPPADDING', (0,1), (-1,-1), 8),
            ('BOTTOMPADDING', (0,1), (-1,-1), 8)
        ]))
        elements.append(pillar_table)
    
    elements.append(PageBreak())
    
    # Posts
    platform_colors = {
        'linkedin': colors.HexColor('#0077b5'),
        'twitter': colors.HexColor('#1da1f2'),
        'instagram': colors.HexColor('#e4405f'),
        'facebook': colors.HexColor('#1877f2'),
        'tiktok': colors.HexColor('#000000')
    }
    
    elements.append(Paragraph(f"Content Library ({len(data['posts'])} Posts)", section_header_style))
    
    for i, post in enumerate(data['posts']):
        platform_color = platform_colors.get(post['platform'], colors.HexColor('#667eea'))
        
        post_header = [[f"Post #{post['post_number']}", post['platform'].upper(), 
                       post['posting_day'], post['posting_time']]]
        
        header_table = Table(post_header, colWidths=[1.5*inch]*4)
        header_table.setStyle(TableStyle([
            ('BACKGROUND', (1,0), (1,0), platform_color),
            ('TEXTCOLOR', (1,0), (1,0), colors.whitesmoke),
            ('BACKGROUND', (0,0), (0,0), colors.HexColor('#f7fafc')),
            ('BACKGROUND', (2,0), (-1,0), colors.HexColor('#f7fafc')),
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('FONTNAME', (0,0), (-1,-1), 'Helvetica-Bold'),
            ('FONTSIZE', (0,0), (-1,-1), 9),
            ('GRID', (0,0), (-1,-1), 1, colors.HexColor('#e2e8f0')),
            ('TOPPADDING', (0,0), (-1,-1), 6),
            ('BOTTOMPADDING', (0,0), (-1,-1), 6)
        ]))
        
        post_elements = [header_table, Spacer(1, 0.08*inch)]
        post_elements.append(Paragraph(f"<b>{post['title']}</b>", normal_style))
        post_elements.append(Paragraph(post['content'], normal_style))
        
        if post['hashtags']:
            hashtags = ' '.join([f'#{h}' for h in post['hashtags']])
            post_elements.append(Paragraph(f'<font color="#667eea"><b>{hashtags}</b></font>', normal_style))
        
        post_elements.append(Paragraph(f'<font color="#11998e"><b>Type: {post["content_type"]}</b></font>', normal_style))
        post_elements.append(Spacer(1, 0.15*inch))
        
        elements.append(KeepTogether(post_elements))
        
        if (i + 1) % 3 == 0 and i < len(data['posts']) - 1:
            elements.append(PageBreak())
    
    elements.append(PageBreak())
    
    if data['hashtag_bank']:
        elements.append(Paragraph("Hashtag Bank", section_header_style))
        hashtag_rows = []
        row = []
        for i, tag in enumerate(data['hashtag_bank'][:25]):
            row.append(f'#{tag}')
            if (i + 1) % 5 == 0:
                hashtag_rows.append(row)
                row = []
        if row:
            while len(row) < 5:
                row.append('')
            hashtag_rows.append(row)
        
        hashtag_table = Table(hashtag_rows, colWidths=[1.3*inch]*5)
        hashtag_table.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#667eea')),
            ('TEXTCOLOR', (0,0), (-1,-1), colors.whitesmoke),
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('FONTNAME', (0,0), (-1,-1), 'Helvetica-Bold'),
            ('GRID', (0,0), (-1,-1), 1, colors.HexColor('#764ba2')),
            ('TOPPADDING', (0,0), (-1,-1), 8),
            ('BOTTOMPADDING', (0,0), (-1,-1), 8)
        ]))
        elements.append(hashtag_table)
    

    if data['posting_schedule']:
        elements.append(Spacer(1, 0.3*inch))
        elements.append(Paragraph("Posting Schedule", section_header_style))
        schedule_data = [['Platform', 'Frequency', 'Best Times', 'Content Type']]
        for item in data['posting_schedule']:
            schedule_data.append([item['platform'], item['frequency'], 
                                 item['best_times'], item['content_type']])
        
        schedule_table = Table(schedule_data, colWidths=[1.5*inch, 1.5*inch, 1.8*inch, 1.7*inch])
        schedule_table.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#11998e')),
            ('TEXTCOLOR', (0,0), (-1,0), colors.whitesmoke),
            ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
            ('BACKGROUND', (0,1), (-1,-1), colors.HexColor('#f8f9fa')),
            ('GRID', (0,0), (-1,-1), 1, colors.HexColor('#e2e8f0')),
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('TOPPADDING', (0,0), (-1,-1), 8),
            ('BOTTOMPADDING', (0,0), (-1,-1), 8)
        ]))
        elements.append(schedule_table)
    
    if data['kpi_targets']:
        elements.append(Spacer(1, 0.3*inch))
        elements.append(Paragraph("KPI Targets", section_header_style))
        kpi_data = [['Metric', 'Target']]
        for kpi in data['kpi_targets']:
            kpi_data.append([kpi['metric'], kpi['target']])
        
        kpi_table = Table(kpi_data, colWidths=[3.5*inch, 3*inch])
        kpi_table.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#38ef7d')),
            ('TEXTCOLOR', (0,0), (-1,0), colors.HexColor('#1a202c')),
            ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
            ('BACKGROUND', (0,1), (-1,-1), colors.HexColor('#f0fdf4')),
            ('TEXTCOLOR', (0,1), (-1,-1), colors.HexColor('#11998e')),
            ('FONTNAME', (0,1), (-1,-1), 'Helvetica-Bold'),
            ('FONTSIZE', (0,1), (-1,-1), 12),
            ('GRID', (0,0), (-1,-1), 1.5, colors.HexColor('#11998e')),
            ('ALIGN', (0,0), (-1,-1), 'CENTER'),
            ('TOPPADDING', (0,0), (-1,-1), 10),
            ('BOTTOMPADDING', (0,0), (-1,-1), 10)
        ]))
        elements.append(kpi_table)
    
    doc.build(elements, onFirstPage=create_header_footer, onLaterPages=create_header_footer)
    return output_path