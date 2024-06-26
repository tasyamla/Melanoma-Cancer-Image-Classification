Project ini dibuat untuk mengidentifkasi Kanker Kulit Melanoma yang dapat dibedakan antara `Melanoma Jinak (Benign) dan Melanoma Ganas(Malignant)` menggunakan konsep model Computer Vision dengan Artificial Neural Network.

Langkah-Langkah yang dilakukan:
   1. Import Libraries
      > *Cell* berisi semua *library* yang digunakan dalam *project*.
   
   2. Data Loading
      > Bagian ini berisi proses penyiapan data sebelum dilakukan eksplorasi data lebih lanjut. Proses Data Loading dapat berupa memberi nama baru untuk setiap kolom, mengecek ukuran dataset, dll.
   
   3. Exploratory Data Analysis (EDA)
      > Bagian ini berisi explorasi data pada dataset diatas dengan menggunakan query, grouping, visualisasi sederhana, dan lain sebagainya.

   4. Feature Engineering
      > Bagian ini berisi proses penyiapan data untuk proses pelatihan model, seperti pembagian data menjadi train-val-test, preprocessing, dan proses-proses lain yang dibutuhkan.   
   
   5. ANN Training (Sequential API/Functional API)
      
      v.1. Model Definition
      > Bagian ini berisi untuk mendefinisikan model. 

      v.2. Model Training
      > Bagian ini hanya berisi code untuk melatih model dan output yang dihasilkan.
      
      v.3. Model Evaluation
      > Bagian ini dilakukan evaluasi model yang harus menunjukkan bagaimana performa model berdasarkan metrics yang dipilih. Hal ini harus dibuktikan dengan visualisasi tren performa dan/atau tingkat kesalahan model. 

   6. ANN Improvement (Sequential API/Functional API)
      
      vi.1. Model Definition
      > Bagian ini berisi cell untuk mendefinisikan model.

      vi.2. Model Training
      > Bagian ini berisi code untuk melatih model dan output yang dihasilkan. 
      
      vi.3. Model Evaluation
      > Pada bagian ini, dilakukan evaluasi model yang harus menunjukkan bagaimana performa model berdasarkan metrics yang dipilih. Hal ini harus dibuktikan dengan visualisasi tren performa dan/atau tingkat kesalahan model. 
   
   8. Model Saving
      > Bagian ini melakukan proses penyimpanan model dan file-file lain yang terkait dengan hasil proses pembuatan model.
   
   9. Model Inference
      > Model yang sudah dilatih akan dicoba pada data yang bukan termasuk ke dalam train-set, val-set, ataupun test-set. 
   
   10. Pengambilan Kesimpulan
       > Bagian ini berisi kesimpulan yang mencerminkan hasil yang didapat dengan *objective* yang sudah ditulis di bagian pengenalan.
