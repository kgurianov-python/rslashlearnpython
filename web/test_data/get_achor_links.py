import random
from yattag import Doc

doc, tag, text = Doc().tagtext()
LOREM = ["""Maecenas ligula urna, tincidunt quis hendrerit in, hendrerit et massa. Proin dictum felis a vehicula gravida. Curabitur vel purus fermentum, sagittis quam nec, ultrices sem. Nam id gravida ante. Etiam id libero quam. Etiam in enim eros. Suspendisse vel malesuada tellus, vitae tincidunt orci. Fusce sit amet diam diam. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Curabitur lectus erat, placerat et pharetra eu, vehicula pulvinar elit. Integer tellus lectus, vestibulum in justo in, ultrices laoreet risus. Nunc nisl velit, varius at dui vitae, vehicula vehicula nibh.""",
         "Suspendisse eget molestie turpis, id placerat nunc. Cras tempor mauris vel quam elementum molestie. Sed venenatis eget quam in ultrices. Nam tristique, felis pellentesque congue posuere, quam enim porta odio, id scelerisque velit ante ut mi. Suspendisse quis fermentum elit. Fusce dapibus metus vitae sagittis dignissim. In quis dolor ultrices, convallis lorem eu, venenatis ligula. Cras suscipit condimentum mauris, sit amet molestie lacus dictum vel. Nulla ut erat auctor, vulputate magna eget, volutpat ligula. Duis pharetra purus eros. Nunc ornare tincidunt leo eu pretium. Quisque aliquet lorem porttitor aliquam rhoncus.",
         "Nulla aliquet, ante vel ullamcorper pharetra, risus sem tempor nisl, quis accumsan lorem massa sed mauris. Integer risus erat, gravida ac ante ac, sodales maximus elit. Vestibulum eget euismod risus. Suspendisse vitae elit id tortor maximus bibendum. Fusce in ante eget felis dignissim blandit eget ac dolor. Curabitur efficitur enim ac justo posuere dictum. Etiam feugiat eleifend ante, nec scelerisque ipsum fringilla blandit. In gravida urna et magna pulvinar feugiat. Vestibulum fringilla iaculis elit ac auctor. Mauris faucibus lectus nec mattis porta. Curabitur tincidunt vehicula augue, tincidunt consequat lectus lobortis in. Nam posuere risus eu malesuada aliquet. Vestibulum metus justo, consequat non massa nec, convallis gravida magna.",
         "Sed at nibh ut lectus tincidunt efficitur. Quisque ultricies, lorem nec tristique volutpat, lacus justo tempor enim, non dignissim libero risus at sem. Aliquam vel eros iaculis, varius nulla eget, egestas tellus. Nam efficitur mollis nunc, ac malesuada felis blandit quis. Nunc eget nisi a eros ullamcorper eleifend vitae nec risus. Sed quis ex est. Mauris vehicula, velit vitae sagittis mollis, tellus purus gravida ex, lobortis dapibus metus urna ut enim. Duis eget ex nunc. Mauris non libero vel libero convallis eleifend in ut ante. Donec vel convallis magna, tristique pulvinar sem. Aliquam eu massa id neque dictum ultricies ac nec lectus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Morbi dolor diam, tincidunt id mi sit amet, malesuada dapibus ante. Cras erat metus, tempor vitae tincidunt vel, euismod et ex. Aliquam ac lorem maximus, dictum nisi eget, luctus enim.",
         "Ut nec finibus diam. Donec eu maximus nulla, vel lobortis nulla. Mauris faucibus fringilla ligula ac accumsan. Ut venenatis sapien id urna fermentum ultrices. Mauris viverra lorem est, eget pharetra felis sollicitudin et. Ut quis magna a turpis eleifend sagittis. Pellentesque lobortis massa pellentesque felis euismod, a viverra eros faucibus. Aliquam pellentesque velit quam, a eleifend diam finibus venenatis."]

with tag('html'):
    with tag('body'):
        with tag('div', id='top'):
            for i in range(20):
                ids = 'top'
                hrefs = "level1"
                with tag('p', id=f'{ids}-{i:04}'):
                    with tag('h5'):
                        text(f'HEADER {ids}-{i:04}')
                    with tag('a', href=f'#{hrefs}-{i:04}'):
                        text(f'Link to {hrefs}-{i:04}')
                    with tag('p'):
                        text(random.choice(LOREM))
            for i in range(20):
                ids = 'level1'
                hrefs = "level2"
                with tag('p', id=f'{ids}-{i:04}'):
                    with tag('h5'):
                        text(f'HEADER {ids}-{i:04}')
                    with tag('a', href=f'#{hrefs}-{i:04}'):
                        text(f'Link to {hrefs}-{i:04}')
                    with tag('p'):
                        text(random.choice(LOREM))



f = open('out.html', 'w')
f.write(doc.getvalue())
f.close()
