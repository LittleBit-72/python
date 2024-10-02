import cv2 

# Membaca citra dari file 'gundam.jpg'
image = cv2.imread('gundam.jpg')

# Memeriksa apakah citra berhasil dibaca
if image is None:
    print("Gagal membaca citra. Pastikan file 'gundam.jpg' ada di direktori yang benar.")
    exit()

# Mengonversi citra berwarna ke citra grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 

# Mengaplikasikan threshold untuk menghasilkan citra monokrom
# Parameter 127 adalah nilai threshold; 255 adalah nilai maksimal untuk piksel
# cv2.THRESH_BINARY menentukan jenis thresholding
ret, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

# Menampilkan citra asli
cv2.imshow('Asli', image)

# Menampilkan citra grayscale
cv2.imshow('Gambar Grayscale', gray_image)

# Menampilkan citra monokrom (biner)
cv2.imshow('Citra Monokrom', binary_image)

# Menunggu hingga ada input dari keyboard
cv2.waitKey(0)

# Menutup semua jendela yang dibuka
cv2.destroyAllWindows()
