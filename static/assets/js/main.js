$(document).on("click", ".chat", function () {
  $(".chat-list").children(".chat").removeClass("active");
  $(this).addClass("active");
});

var chatBox = $(".chatBx");
chatBox.animate({ scrollTop: chatBox.prop("scrollHeight") });

var form = $("#form");
var sender = $("#myID").val();
var receiver = $("#friendID").val();

const socket = new WebSocket(`ws://127.0.0.1:8000/ws/chat/${receiver}/`);

socket.onopen = (e) => {
  form.on("submit", function (e) {
    e.preventDefault();
    var message = $("#messageBox").val();
    if (receiver) {
      socket.send(JSON.stringify({ message: message }));
    } else {
      alert("Please Select a Friend");
    }
    $("#messageBox").val(null);
  });
};

function addMessageElement(data) {
  var element = "";
  if (sender == data["receiver"]) {
    element = `
      <div class="msg msg-frnd">
         <p>${data["message"]}<br> <span>12:15</span></p>
       </div>
    `;
  } else {
    element = `
     <div class="msg msg-me">
         <p>${data["message"]}<br>
            <span>12:15</span>
         </p>
      </div>

    `;
  }
  return element;
}
socket.onmessage = (e) => {
  var data = JSON.parse(e.data);
  console.log(data);
  var element = addMessageElement(data);
  if (receiver == data["sender"]) {
    console.log("ok");
  }
  chatBox.append(element);

  chatBox.animate({ scrollTop: chatBox.prop("scrollHeight") });
};
socket.onclose = (e) => {
  console.log(e);
};
