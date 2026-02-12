#!/usr/bin/env python3
"""
Update README.md and README_EN.md with dynamic content from templates.
Focuses on Machine Learning and Python quotes with bilingual support.
"""

import re
from pathlib import Path
import random

# ML/AI and Python related quotes - English
ML_QUOTES_EN = [
    ("The best way to predict the future is to invent it.", "Alan Kay"),
    ("Machine learning is the field of study that gives computers the ability to learn without being explicitly programmed.", "Arthur Samuel"),
    ("Simple is better than complex.", "Tim Peters (Zen of Python)"),
    ("Explicit is better than implicit.", "Tim Peters (Zen of Python)"),
    ("Readability counts.", "Tim Peters (Zen of Python)"),
    ("Data is the new oil.", "Clive Humby"),
    ("Without big data analytics, companies are blind and deaf.", "Jeffrey Weiner"),
    ("In God we trust, all others bring data.", "W. Edwards Deming"),
    ("The goal of AI is to enable machines to do things that would require intelligence if done by humans.", "John McCarthy"),
    ("Python is an experiment in how much freedom programmers need.", "Guido van Rossum"),
    ("Code is read more often than it is written.", "Guido van Rossum"),
    ("Deep learning is a superpower. With it you can make a computer see, synthesize novel art, translate languages, and more.", "Andrew Ng"),
    ("The question of whether a computer can think is no more interesting than the question of whether a submarine can swim.", "Edsger W. Dijkstra"),
    ("Any sufficiently advanced technology is indistinguishable from magic.", "Arthur C. Clarke"),
    ("The development of full artificial intelligence could spell the end of the human race.", "Stephen Hawking"),
    ("We are suffering from an overload of data and not enough wisdom.", "Jay Walker"),
    ("The electric light did not come from the continuous improvement of candles.", "Oren Harari"),
    ("A computer would deserve to be called intelligent if it could deceive a human into believing that it was human.", "Alan Turing"),
]

# ML/AI and Python related quotes - Chinese
ML_QUOTES_CN = [
    ("预测未来的最好方式就是创造它。", "艾伦·凯 (Alan Kay)"),
    ("机器学习是研究计算机如何不需要明确编程就能进行学习的领域。", "亚瑟·塞缪尔 (Arthur Samuel)"),
    ("简单胜于复杂。", "蒂姆·彼得斯 (Python之禅)"),
    ("明了胜于晦涩。", "蒂姆·彼得斯 (Python之禅)"),
    ("可读性很重要。", "蒂姆·彼得斯 (Python之禅)"),
    ("数据是新石油。", "克莱夫·汉比 (Clive Humby)"),
    ("没有大数据分析，公司就是盲人和聋子。", "杰弗里·韦纳 (Jeffrey Weiner)"),
    ("除了上帝，每个人都必须带数据来。", "W·爱德华兹·戴明 (W. Edwards Deming)"),
    ("人工智能的目标是使机器能够完成原本需要人类智能才能完成的事情。", "约翰·麦卡锡 (John McCarthy)"),
    ("Python 是一个关于程序员需要多少自由的实验。", "吉多·范罗苏姆 (Guido van Rossum)"),
    ("代码的阅读次数远多于编写次数。", "吉多·范罗苏姆 (Guido van Rossum)"),
    ("深度学习是一种超能力。有了它，你可以让计算机看、合成新颖的艺术作品、翻译语言等等。", "吴恩达 (Andrew Ng)"),
    ("计算机能否思考的问题并不比潜艇能否游泳的问题更有趣。", "艾兹赫尔·戴克斯特拉 (Edsger W. Dijkstra)"),
    ("任何足够先进的技术都与魔法无异。", "亚瑟·克拉克 (Arthur C. Clarke)"),
    ("完整人工智能的发展可能意味着人类种族的终结。", "史蒂芬·霍金 (Stephen Hawking)"),
    ("我们正遭受数据过剩、智慧不足的困扰。", "杰伊·沃克 (Jay Walker)"),
    ("电灯并非来自蜡烛的持续改进。", "奥伦·哈拉里 (Oren Harari)"),
    ("如果一台计算机能够欺骗人类，使人类相信它是人类，那么它就值得被称为智能。", "艾伦·图灵 (Alan Turing)"),
]


def get_random_ml_quote(lang='en'):
    """获取随机 ML/Python 名言"""
    quotes = ML_QUOTES_EN if lang == 'en' else ML_QUOTES_CN
    return random.choice(quotes)


def update_readme(template_path, readme_path, quote, author, lang='en'):
    """使用模板更新 README 文件"""
    if not template_path.exists():
        print(f"❌ Template file not found: {template_path}")
        return False

    # 读取模板
    content = template_path.read_text(encoding="utf-8")

    # 替换 ML/Python quote (替换所有匹配的占位符)
    replacement = f"<!-- PYTHON-QUOTE:START -->\n\n> *\"{quote}\"*  \n> — **{author}**\n\n<!-- PYTHON-QUOTE:END -->"
    content = re.sub(
        r"<!-- PYTHON-QUOTE:START -->.*?<!-- PYTHON-QUOTE:END -->",
        replacement,
        content,
        flags=re.DOTALL,
    )

    # 写入 README 文件
    readme_path.write_text(content, encoding="utf-8")
    lang_name = "English" if lang == 'en' else "简体中文"
    print(f"✅ {readme_path.name} ({lang_name}) updated successfully!")
    print(f"💭 Quote: \"{quote[:50]}...\" — {author}")
    return True


def main():
    """主函数：更新中文和英文 README"""
    base_path = Path(".")

    # 英文版
    template_en = base_path / "README_EN.template.md"
    readme_en = base_path / "README_EN.md"
    quote_en, author_en = get_random_ml_quote('en')
    update_readme(template_en, readme_en, quote_en, author_en, 'en')

    # 中文版
    template_cn = base_path / "README.template.md"
    readme_cn = base_path / "README.md"
    quote_cn, author_cn = get_random_ml_quote('cn')
    update_readme(template_cn, readme_cn, quote_cn, author_cn, 'cn')

    print("\n🎉 All README files have been updated!")


if __name__ == "__main__":
    main()
