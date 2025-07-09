import random

def generate_quiz_from_text(text):
    """
    根据输入文本随机生成一道选择题。
    逻辑：
    - 先将文本按句号分割，随机选一句。
    - 再从该句随机选一个词替换为空白。
    - 生成4个选项，其中一个是正确答案，3个是其他随机词。
    """
    if not text or '。' not in text:
        return None
    
    sentences = [s.strip() for s in text.split('。') if s.strip()]
    if not sentences:
        return None

    question_sentence = random.choice(sentences)
    words = question_sentence.split()
    if len(words) < 2:
        return None

    question_word = random.choice(words)
    
    # 生成错误选项，从句子中排除正确答案，避免重复
    wrong_choices = [w for w in words if w != question_word]
    if len(wrong_choices) < 3:
        # 如果词不够，补充一些常用词
        wrong_choices += ['选项A', '选项B', '选项C']

    choices_pool = random.sample(wrong_choices, 3)
    choices_pool.append(question_word)
    random.shuffle(choices_pool)
    
    choices = dict(zip(['A', 'B', 'C', 'D'], choices_pool))
    
    # 找正确答案对应的选项字母
    answer = [key for key, val in choices.items() if val == question_word][0]
    
    quiz = {
        'question': question_sentence.replace(question_word, '____'),
        'choices': choices,
        'answer': answer
    }
    return quiz
