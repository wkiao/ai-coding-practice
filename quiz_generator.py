import random

# 输入一段文本，自动生成一道选择题
def generate_quiz_from_text(text):
    # 从文本中随机抽取一个句子
    sentences = text.split('。')
    if len(sentences) > 1:
        question_sentence = random.choice(sentences)
        # 从句子中随机抽取一个词语
        words = question_sentence.split(' ')
        if len(words) > 1:
            question_word = random.choice(words)
            # 构建选择题
            choices = ['A', 'B', 'C', 'D']
            random.shuffle(choices)
            quiz = {
                'question': question_sentence.replace(question_word, '____'),
                'choices': dict(zip(choices, [question_word] + random.sample(words, 3))),
                'answer': choices[0]  # 注意正确答案应对应替换词
            }
            return quiz
    return None

