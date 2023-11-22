course_subjects = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lingua']
subject_score = {}


def put_score(subj_lst):
    for i in subj_lst:
        score = float(input(f'Introduce tu nota en {i}\n'))
        subject_score[i] = score

    for i, j in subject_score.items():
        print(f"En {i} sacaste un {j}")


put_score(course_subjects)


