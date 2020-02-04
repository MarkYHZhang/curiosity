from django.db import models


class Post(models.Model):
    question = models.CharField(max_length=1000)
    answer = models.TextField(blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    replacement_dict = {
        '*': ("<strong>", "</strong>"),  # *bold*
        '_': ("<em>", "</em>"),  # _underline _
        '^': ("<li>", "</li>"),  # ^bullet^
        '!': ("<h2>", "</h2>"),  # !important!
        '~': ("", "<hr>"),      # ~~ horizontal line
    }

    @property
    def formatted_answer(self):
        flag_dict = {key: False for key in self.replacement_dict.keys()}
        result = ""
        for c in self.answer:
            if c in self.replacement_dict.keys():
                if not flag_dict[c]:
                    result += self.replacement_dict[c][0]
                else:
                    result += self.replacement_dict[c][1]
                flag_dict[c] = not flag_dict[c]
            else:
                result += c
        return result

    def peek(self):
        return self.formatted_answer[:500]

    def __str__(self):
        return self.question

    class Meta():
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'