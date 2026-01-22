import openAI
import genAI


def test_openai_text_search():
    input_text = "What are the benefits of using AI in healthcare?"
    result = openAI.get_text_search(input_text, source='env')
    print("OpenAI Text Search Result:", result)
    assert isinstance(result, str)
    assert "AI" in result
    print("openAI Text Search passed all tests.")

def test_genai_text_search():
    input_text = "What are the benefits of using AI in healthcare?"
    result = genAI.get_text_search(input_text, source='env')
    print("GenAI Text Search Result:", result)
    assert isinstance(result, str)
    assert "AI" in result
    print("genAI Text Search passed all tests.")

def main():
    print("Running openAI tests...")
    print("=" * 50)
    test_openai_text_search()
    
    print("\nRunning genAI tests...")
    print("=" * 50)
    test_genai_text_search()


if __name__ == "__main__":
    main()
