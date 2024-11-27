from util import openai as gpt

def main():
    client, gpt_model = gpt.get_image_client()

    # Prompt for image description
    description = input('Prompt ("exit" to quit): ')
    if description == 'exit':
        return

    # Prompt for number of images to create
    while True:
        count = input('Number of images ("exit" to quit): ')
        if count == 'exit':
            return

        try:
            count = int(count)
            if count < 1 or count > 10:
                raise ValueError
            break
        except ValueError:
            print('Enter number between 1-10.')
            continue

    # Prompt for image size
    while True:
        if gpt_model == 'dall-e-2':
            size = input('Image size [256, 512, 1024] ("exit" to quit): ')
        else:
            size = input('Image aspect ["square" = 1024x1024, "wide" = 1792x1024, "tall" = 1024x1792] ("exit" to quit): ')
        if size == 'exit':
            return
        elif gpt_model == 'dall-e-3':
            if size[0] not in ['s', 'w', 't']:
                print('Enter "square", "wide", or "tall".')
                continue
            else:
                sizer = {'s': "1024x1024", 'w': "1792x1024", 't': "1024x1792"}
                img_size = sizer[size[0]]
        else:
            try:
                isize = int(size)
                if isize not in [256, 512, 1024]:
                    raise ValueError
                img_size = f"{isize}x{isize}"
                break
            except ValueError:
                print('Enter 256, 512, or 1024.')
                continue

    # Generate images
    try:
        response = client.images.generate(
            prompt = description,
            n = count,
            size = img_size,
            model = gpt_model,
        )
    except Exception as e:
        print(f'Error: {e}')
        return

    if response.data:
        print(f'Generated {len(response.data)} images:')
        for i, image in enumerate(response.data):
            print(f'Image {i + 1}: {image.url}')
# end def: main

if __name__ == '__main__':
    main()
# end if: __name__
