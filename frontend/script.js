const API = "https://mink-farm-system-production-4626.up.railway.app";

async function load() {
  const res = await fetch(API + "/minks");
  const data = await res.json();

  const list = document.getElementById("list");
  list.innerHTML = "";

  data.forEach(m => {
    list.innerHTML += 
      <li>
        ${m.female_no} - ${m.shed}
        <button onclick="del(${m.id})">X</button>
      </li>
    ;
  });
}

async function del(id) {
  await fetch(API + "/minks/" + id, { method: "DELETE" });
  load();
}

document.getElementById("form").onsubmit = async (e) => {
  e.preventDefault();

  await fetch(API + "/minks", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      female_no: female_no.value,
      year: +year.value,
      quality: quality.value,
      last_year_kids: +last.value,
      this_year_kids: +this.value,
      shed: shed.value
    })
  });

  load();
};

load();
