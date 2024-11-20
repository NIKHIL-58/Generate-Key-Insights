# 📚 **Generate Key Insights API**  

![FastAPI](https://img.shields.io/badge/FastAPI-%F0%9F%9A%80-brightgreen)  
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)  
![License](https://img.shields.io/badge/license-MIT-informational)  

### 🚀 **Extract meaningful insights from long stories effortlessly!**

The **Generate Key Insights API** is a powerful FastAPI-based application designed to analyze long texts and extract specific insights such as **career guidance**, **productivity hacks**, or **life tips**, tailored to your query.

---

## 🌟 **Features**

- 📝 **Text Cleaning**: Removes unwanted characters and normalizes input text.
- 🎯 **Keyword Extraction**: Focus on the most relevant parts of the story based on your topic.
- 💡 **Insight Summarization**: Generate concise summaries for better readability.
- ⚡ **FastAPI Framework**: High-performance, modern, and asynchronous backend.

---

## 🛠️ **Project Structure**

```plaintext
generate_key_insights/
├── app/
│   ├── main.py              # FastAPI application entry point
│   ├── routes.py            # API routes
│   ├── services.py          # Core business logic
│   ├── models.py            # Data models for API requests and responses
│   └── utils.py             # Utility functions (cleaning, keyword extraction)
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## ⚙️ **Setup and Installation**

### **Prerequisites**
- Python 3.8 or higher  
- Pip (Python package manager)

### **Installation Steps**
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/generate-key-insights.git
   cd generate-key-insights
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For macOS/Linux
   .\venv\Scripts\activate   # For Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Download NLTK data:
   ```python
   import nltk
   nltk.download('stopwords')
   ```

---

## 🚀 **Run the Application**

Start the FastAPI server:
```bash
uvicorn app.main:app --reload
```

Access the interactive API documentation at:  
👉 **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

---

## 📊 **API Usage**

### **Endpoint**: `/generate-insights`  
**Method**: `POST`  
**Description**: Extract specific insights from a long story.

#### **Request Body**:
```json
{
  "story": "In today's fast-paced world, achieving a balance between productivity and personal growth is critical. Successful individuals often prioritize time management, breaking down large goals into manageable steps. They emphasize creating a daily routine that incorporates focus periods and regular breaks to avoid burnout. Career growth can also benefit from these strategies. For instance, networking and consistent skill-building are crucial for professionals looking to advance. Furthermore, adopting life hacks like keeping a gratitude journal or practicing mindfulness can significantly enhance well-being, making individuals more resilient in challenging situations.",
  "prompt": "productivity"
}
```

#### **Response**:
```json
{
  "insights": [
    "Focus on time management by setting clear priorities.",
    "Break larger tasks into smaller, manageable steps."
  ]
}
```

---

## 🧪 **Testing**

Run unit tests to verify functionality:
```bash
pytest tests/
```

---

## 📂 **Technologies Used**

- **Python** 🐍  
- **FastAPI** 🚀  
- **Transformers** 🤗 (for summarization)  
- **RAKE-NLTK** 📜 (for keyword extraction)  

---

## 🌐 **Contributing**

We welcome contributions!  
1. Fork the repository.  
2. Create a feature branch:  
   ```bash
   git checkout -b feature/your-feature
   ```
3. Commit your changes and create a pull request.  

---

## 📜 **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🛠️ **Future Enhancements**

- 🌍 Support for multilingual insights generation.  
- 🧠 Integration with GPT models for advanced summarization.  
- 📊 Dashboard for visualizing extracted insights.  

---

### 🎉 **Happy Coding!**  

> 🚀 *"Transforming stories into actionable insights, one query at a time."*

--- 
