# 📅 MultiAgent Content Calendar Generator

> **Transform your social media strategy in minutes with AI-powered content planning**

Generate a complete 30-day social media content calendar with engaging posts, strategic planning, and professional PDF reports - all powered by local AI using Ollama and CrewAI.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![CrewAI](https://img.shields.io/badge/CrewAI-Latest-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

### 🎯 Smart Content Generation
- **30+ Platform-Optimized Posts** - Tailored content for Instagram, LinkedIn, Twitter, Facebook, and TikTok
- **AI-Powered Insights** - Multiple specialized AI agents working together to create cohesive content
- **Brand Voice Matching** - Content that aligns with your unique brand personality

### 📊 Professional PDF Reports
- **Colorful, Print-Ready Design** - Beautiful gradient headers and professional typography
- **Comprehensive Tables** - Stats overview, content pillars, posting schedule, and KPI targets
- **Platform-Specific Color Coding** - Visual distinction for each social media platform
- **Multi-Page Layout** - Organized sections with automatic pagination

### 🤖 Multi-Agent AI System
- **Brand Analyst** - Deep-dives into your brand voice and target audience
- **Trend Researcher** - Identifies relevant hashtags and viral content opportunities
- **Content Strategist** - Develops posting schedules and content themes
- **Copywriter** - Crafts engaging, platform-specific posts
- **Calendar Packager** - Compiles everything into a professional deliverable

### 🎨 User-Friendly Interface
- **Streamlit Web App** - Clean, intuitive interface with no coding required
- **Real-Time Generation** - Watch as your content calendar is created
- **One-Click Download** - Export your calendar as a professional PDF

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- [Ollama](https://ollama.ai/) installed and running
- Llama 3.2 model pulled in Ollama

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/OmarrAymann/Multi_Agent-Content_Creator
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Pull the AI model**
```bash
ollama pull llama3.2:3b
```

4. **Run the application**
```bash
streamlit run app.py
```

5. **Open your browser**
Navigate to `http://localhost:8501`

## 📖 Usage Guide

### Step 1: Fill in Brand Information

Provide details about your brand:
- **Brand Name** - Your company or personal brand name
- **Industry** - Fashion, tech, food, fitness, etc.
- **Brand Voice** - Professional, casual, humorous, inspirational
- **Target Audience** - Demographics, interests, pain points

### Step 2: Define Your Goals

Specify what you want to achieve:
- **Content Goals** - Engagement, awareness, sales, education
- **Platforms** - Select from Instagram, LinkedIn, Twitter, Facebook, TikTok
- **Posting Frequency** - 1-5 posts per week
- **Content Themes** - Topics you want to focus on

### Step 3: Add Details (Optional)

Enhance your calendar with:
- **Brand Values** - What your brand stands for
- **Competitors** - For competitive analysis
- **Upcoming Events** - Product launches, promotions
- **Topics to Avoid** - Content restrictions

### Step 4: Generate & Download

1. Click "**Generate content calendar**"
2. Wait 1-2 minutes while AI agents collaborate
3. Click "**generate pdf**" to create your report
4. Download your professional content calendar!

## 📁 Project Structure

```
ai-content-calendar/
│
├── app.py                  # Main Streamlit application
├── crew.py                 # CrewAI orchestration
├── agents.py               # AI agent definitions
├── content_tasks.py        # Task definitions for agents
├── file_generator.py       # PDF generation engine
├── model_config.py         # LLM configuration
├── requirements.txt        # Python dependencies
└── README.md              # This file
```

## 🛠️ Technical Architecture

### AI Multi-Agent System

```
User Input
    ↓
Brand Analyst → Analyzes brand voice & audience
    ↓
Trend Researcher → Identifies opportunities
    ↓
Content Strategist → Plans calendar structure
    ↓
Copywriter → Creates 30+ posts
    ↓
Calendar Packager → Compiles final output
    ↓
PDF Generator → Professional report
```

### Technology Stack

- **Frontend**: Streamlit (Python web framework)
- **AI Framework**: CrewAI (Multi-agent orchestration)
- **Language Model**: Llama 3.2 via Ollama
- **PDF Generation**: ReportLab
- **Styling**: Custom CSS with gradient designs

## 📊 Sample Output

Your generated PDF includes:

### 📈 Stats Dashboard
- Total posts count
- Number of platforms
- Posts per week
- Content themes

### 🎯 Content Pillars
Strategic themes guiding your content (4-6 pillars)

### 📝 Complete Post Library
30+ posts with:
- Platform-specific formatting
- Catchy titles
- Engaging copy (50+ words each)
- 5-10 relevant hashtags
- Optimal posting times
- Content type classification

### 🏷️ Hashtag Bank
20-30 curated hashtags for maximum reach

### 📅 Posting Schedule
Platform-by-platform posting guide with:
- Frequency recommendations
- Best posting times
- Content type focus

### 🎯 KPI Targets
6-8 metrics to track success:
- Engagement rate
- Follower growth
- Reach
- Click-through rate
- And more...

## 🎨 Customization

### Change the AI Model

Edit `model_config.py`:
```python
language_model = LLM(
    model="ollama/llama3.2:3b",  # Change to your preferred model
    base_url="http://localhost:11434",
    temperature=0.9,
)
```

```

### Customize Agent Behavior

Edit agent roles in `agents.py` to change their expertise and focus.



## 🙏 Acknowledgments

- **CrewAI** - For the amazing multi-agent framework
- **Ollama** - For local LLM hosting
- **Streamlit** - For the intuitive web framework
- **ReportLab** - For professional PDF generation
- **Meta** - For the Llama models


