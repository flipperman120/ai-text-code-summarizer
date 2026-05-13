"""
Example usage of AI Text & Code Summarizer
"""

from summarizer import Summarizer


def example_1_summarize_article():
    """Example 1: Summarize a news article"""
    print("\n" + "="*60)
    print("EXAMPLE 1: Summarize a News Article")
    print("="*60)
    
    article = """
    Artificial intelligence has revolutionized many industries over the past decade.
    From healthcare to finance, AI algorithms are making decisions that were previously
    made only by humans. Machine learning models can now recognize patterns in data that
    humans might miss, leading to more accurate diagnoses, better fraud detection, and
    personalized recommendations. However, with great power comes great responsibility.
    As AI systems become more prevalent, concerns about bias, privacy, and job displacement
    have come to the forefront. Researchers and policymakers are working together to ensure
    that AI development remains ethical and beneficial for society as a whole.
    """
    
    summarizer = Summarizer()
    summary = summarizer.summarize_text(article, max_length=80)
    
    print("\nOriginal Text:")
    print(article)
    print("\nSummary:")
    print(summary)


def example_2_summarize_python_code():
    """Example 2: Summarize Python code"""
    print("\n" + "="*60)
    print("EXAMPLE 2: Summarize Python Code")
    print("="*60)
    
    python_code = """
    def quicksort(arr):
        if len(arr) <= 1:
            return arr
        
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        
        return quicksort(left) + middle + quicksort(right)
    
    # Example usage
    my_array = [3, 6, 8, 10, 1, 2, 1]
    sorted_array = quicksort(my_array)
    print(sorted_array)
    """
    
    summarizer = Summarizer()
    summary = summarizer.summarize_code(python_code, max_length=80)
    
    print("\nOriginal Code:")
    print(python_code)
    print("\nSummary:")
    print(summary)


def example_3_summarize_javascript():
    """Example 3: Summarize JavaScript code"""
    print("\n" + "="*60)
    print("EXAMPLE 3: Summarize JavaScript Code")
    print("="*60)
    
    js_code = """
    async function fetchUserData(userId) {
        try {
            const response = await fetch(`/api/users/${userId}`);
            if (!response.ok) {
                throw new Error('Failed to fetch user data');
            }
            const userData = await response.json();
            return userData;
        } catch (error) {
            console.error('Error fetching user:', error);
            return null;
        }
    }
    
    fetchUserData(123).then(user => {
        if (user) {
            console.log('User:', user.name);
        }
    });
    """
    
    summarizer = Summarizer()
    summary = summarizer.summarize_code(js_code, max_length=80)
    
    print("\nOriginal Code:")
    print(js_code)
    print("\nSummary:")
    print(summary)


def example_4_custom_parameters():
    """Example 4: Using custom parameters"""
    print("\n" + "="*60)
    print("EXAMPLE 4: Custom Summary Length")
    print("="*60)
    
    text = """
    Cloud computing has fundamentally changed how businesses deploy and manage applications.
    Instead of maintaining expensive physical servers, companies can now leverage scalable
    cloud infrastructure provided by major providers like AWS, Azure, and Google Cloud.
    This shift has enabled startups to compete with established enterprises by reducing
    upfront infrastructure costs. Cloud services offer flexibility, reliability, and access
    to cutting-edge technologies without the burden of hardware maintenance. Additionally,
    cloud platforms provide built-in security features, automatic scaling, and disaster
    recovery capabilities that would be extremely expensive to implement on-premises.
    """
    
    summarizer = Summarizer()
    
    print("\nShort Summary (max_length=50):")
    short_summary = summarizer.summarize_text(text, max_length=50, min_length=20)
    print(short_summary)
    
    print("\nMedium Summary (max_length=100):")
    medium_summary = summarizer.summarize_text(text, max_length=100, min_length=40)
    print(medium_summary)
    
    print("\nLong Summary (max_length=150):")
    long_summary = summarizer.summarize_text(text, max_length=150, min_length=60)
    print(long_summary)


def example_5_batch_summary():
    """Example 5: Batch summarize multiple contents"""
    print("\n" + "="*60)
    print("EXAMPLE 5: Batch Summarization")
    print("="*60)
    
    contents = [
        {
            'name': 'Article 1',
            'text': 'Python is a versatile programming language known for its readability and simplicity. It is widely used in web development, data science, artificial intelligence, and automation. The large ecosystem of libraries and frameworks makes it easy for developers to build complex applications quickly.',
            'type': 'text'
        },
        {
            'name': 'Article 2',
            'text': 'Blockchain technology underlies cryptocurrencies like Bitcoin and Ethereum. It is a distributed ledger that records transactions across multiple computers, making it resistant to tampering and fraud. Beyond cryptocurrency, blockchain has applications in supply chain management, healthcare, and voting systems.',
            'type': 'text'
        },
        {
            'name': 'Code Snippet',
            'text': 'function factorial(n) { if (n <= 1) return 1; return n * factorial(n - 1); }',
            'type': 'code'
        }
    ]
    
    summarizer = Summarizer()
    
    for item in contents:
        print(f"\n{item['name']}:")
        print(f"Type: {item['type']}")
        
        if item['type'] == 'text':
            summary = summarizer.summarize_text(item['text'], max_length=80)
        else:
            summary = summarizer.summarize_code(item['text'], max_length=80)
        
        print(f"Summary: {summary}")


if __name__ == '__main__':
    print("\n🚀 AI Text & Code Summarizer - Examples")
    
    example_1_summarize_article()
    example_2_summarize_python_code()
    example_3_summarize_javascript()
    example_4_custom_parameters()
    example_5_batch_summary()
    
    print("\n" + "="*60)
    print("✅ All examples completed!")
    print("="*60)
    print("\nFor CLI usage, run: python cli.py --help")
