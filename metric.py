def color_plausibility(img):
    img_np = img[0].cpu().numpy().transpose(1, 2, 0)
    lab = rgb2lab(img_np)
    a_mean, b_mean = np.mean(lab[:, :, 1]), np.mean(lab[:, :, 2])
    a_std, b_std = np.std(lab[:, :, 1]), np.std(lab[:, :, 2])
    dev = np.sqrt(a_mean**2 + b_mean**2)
    chroma_var = abs(a_std - b_std)
    return dev + chroma_var
