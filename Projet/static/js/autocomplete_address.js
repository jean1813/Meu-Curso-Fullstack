$(document).ready(function (){
     $("#zip_code").blur(function () {
             //Nova variavel "Cep" somente com dígitos.
            var cep = $(this).val().replace(/\D/g, '');
            //Verifica se campo Cep possui valor informado.
        if (cep != "") {           
            //Expressão regular para validar o CEP.
            var validacep = /^[0-9]{8}$/;
            //valida o formato do CEP.
            if (validacep.test(cep)) {               
                //Preenche os campos com "..." enquanto consulta webservice.
                $("#address").val("...");
                $("#neighborhood").val("...");
                $("#city").val("...");
                $("#state").val("...");
                //Consulta webservice viacep.com.br/
                $.getJSON("https://viacep.com.br/ws/" + cep + "/json/?callback=?", function(dados) {
                    //alert("funcionando");
                            if (!("erro" in dados)) {
                                //Atualiza os campos com os valores da consulta.
                                $("#address").val(dados.logradouro);
                                $("#neighborhood").val(dados.bairro);
                                $("#city").val(dados.localidade);
                                $("#state").val(dados.uf);
                            } else {
                                //CEP pesquisado não foi encontrado.
                                limpa_formulario_cep()
                                alert("cep não encontrado!")
                            }
                });
            } //end if.
            else {
                 //cep é invalido
                 limpa_formulario_cep();
                 alert("Formato de CEP inválido.")
            }
            //end if.           
        }else{
            //Cep sem valor, limpa formulario.
            limpa_formulario_cep();
        }
     });
     
    function limpa_formulario_cep() {
                //Limpa valores do fomulario de cep.
                $("#address").val("");
                $("#neighborhood").val("");
                $("#city").val("");
                $("#state").val("");
                $("#number").val("");
                $("#complemente").val("");

    }

});






 /**
       
        //Verifica se campo cep possui valor informado.
       // if (cep != "") {
            //Expressão regular para validar o CEP.
            var validacep = /^[0-9]{8}$/;
            //valida o formato do CEP.
            if (validacep.teste(cep)) {
                //Preenche os campos com "..." enquanto consulta webservice.
                $("#address").val("...");
                $("#neighborhood").val("...");
                $("#city").val("...");
                $("#state").val("...");
                //Consulta webservice viacep.com.br/
                $.get.JSON("https://viacep.com.br/ws/" + Cep + "/json/?callback=?", function(dados) {
            )       if (!("erro" in dados))
                    $("#address").val(dados.logradouro);
                    $("#neighborhood").val(dados.bairro);
                    $("#city").val(dados.localidade);
                    $("#state").val(dados.uf);
            }
            else {
                //CEP pesquisado não foi encontrado
                limpa_formulario_cep()
                alert("cep não encontrado")
            }
        });
        //end if.

}
);
*/