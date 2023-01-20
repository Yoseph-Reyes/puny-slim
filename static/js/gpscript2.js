var cont = 0;
var incont = 3;

$(function () {
  val = $("#contador").attr("Value");
  param = $("#param").attr("Value");
  x1 = param.replaceAll("[", "")
  x2 = x1.replaceAll("]", "")
  x3 = x2.replaceAll("'", "")
  parem = x3.split(",")
  console.log(parem)
  if (val != null) {
    $("#obj0").val(parem[2]+" "+parem[3]);
    $("#id0").val(parem[4]);
    val = (parem.length-2)/3;
    console.log(val)
    for (let x = 1; x < val; x++) {
      addRow();
      $("#obj"+x).val(parem[2+incont]+" "+parem[3+incont]);
      $("#id"+x).val(parem[4+incont]);
      incont = incont + 3
    }
  }
  $('[data-toggle="tooltip"]').tooltip();
  $("#obj").val(parem[2]+" "+parem[3]);
  $("#id").val(parem[4]);
});
// AÑADIR FILAS
function addRow() {
  const div = document.createElement('div');
  cont++;
  if (cont > 9) {
    alert("Solo puedes incluir 10 reglas");
  } else {
    console.log(cont);
    div.className = "gestor-de-pruebas-container10";
    div.id = 'container' + cont;

    div.innerHTML = `    
    <input
    type="text"
    id="obj`+ cont + `"
    name="obj`+ cont + `"
    placeholder="Objeto `+ cont + `"
    class="gestor-de-pruebas-textinput3 input"
    />
    <input
    type="text"
    id="id`+ cont + `"
    name="id`+ cont + `"
    placeholder="ID `+ cont + `"
    class="gestor-de-pruebas-textinput4 input"
    />
    <select
    class="gestor-de-pruebas-select"
    name="accion`+ cont + `"
    id="accion`+ cont + `"
    >
    <option value="Input Text">Introducir Texto</option>
    <option value="Input Password">Introducir Contraseña</option>
    <option value="Click Element">Hacer clic en</option>
    <option value="Select From List By Label">
    Seleccionar elemento de la lista
    </option>
    </select>
    <input
      type="text"
      id="var`+ cont + `"
      name="var`+ cont + `"
      placeholder="Variable `+ cont + `"
      class="gestor-de-pruebas-textinput5 input"
    />
    <span  class="gestor-de-pruebas-text12"  onclick=remove()>-</span> `;

    document.getElementById('reglas').appendChild(div);
    document.getElementById('contador').value = cont;
  }

}

function remove() {
  document.getElementById('container' + cont).remove();
  cont--;
  document.getElementById('contador').value = cont;
  console.log(cont);
  if (cont < 0) {
    console.log("No puedes eliminar mas reglas pa");
    cont = 0;
  }
}


