from PIL import Image


def convert_to_pdf(outputFile, path, count):
    imgs = []

    for i in range(0, count):
        img = Image.open(f"{path}page_{i}.png")
        converted = img.convert("RGB")
        imgs.append(converted)

    imgs[0].save(
        fp=outputFile,
        save_all=True,
        append_images=imgs[1:],
    )
