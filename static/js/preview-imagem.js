function previewImage(event) {
    var input = event.target;
    var reader = new FileReader();
    reader.onload = function(){
        var imagemPreviewPerfil = document.getElementById('imagem-preview-perfil');
        var imagemPreviewPost = document.getElementById('imagem-preview-post');
        
        if (imagemPreviewPerfil) imagemPreviewPerfil.src = reader.result;
        if (imagemPreviewPost) imagemPreviewPost.src = reader.result;
    };
    reader.readAsDataURL(input.files[0]);
}