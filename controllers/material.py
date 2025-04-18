from odoo import http
from odoo.http import request

class MaterialController(http.Controller):

    @http.route("/api/material", type="json", auth="user", methods=["GET"])
    def get_materials(self, **args):
        domain = []
        search = args.get("search", "")
        if search:
            domain.append("|")
            domain.append("|")
            domain.append(("code", "ilike", search))
            domain.append(("name", "ilike", search))
            domain.append(("supplier_id.name", "ilike", search))
        type = args.get("type", "")
        if type:
            domain.append(("type", "=", type))
        materials = request.env["keda.material"].sudo().search_read(domain)
        return {"status": 200, "data": materials}

    @http.route("/api/material/<int:id>", type="json", auth="user", methods=["GET"])
    def get_material(self, id):
        material = request.env["keda.material"].sudo().browse(id)
        if not material.exists():
            return {"status": 404, "message": "Material not found"}
        return {"status": 200, "data": material.read()[0]}

    @http.route("/api/material", type="json", auth="user", methods=["POST"])
    def create_material(self, **args):
        try:
            material = request.env["keda.material"].sudo().create(args)
            return {"status": 201, "message": "Material created", "data": material.read()[0]}
        except Exception as e:
            return {"status": 400, "error": str(e)}

    @http.route("/api/material/<int:id>", type="json", auth="user", methods=["PUT"])
    def update_material(self, id, **args):
        material = request.env["keda.material"].sudo().browse(id)
        if not material.exists():
            return {"status": 404, "message": "Material not found"}
        try:
            material.write(args)
            return {"status": 200, "message": "Material updated", "data": material.read()[0]}
        except Exception as e:
            return {"status": 400, "error": str(e)}

    @http.route("/api/material/<int:id>", type="json", auth="user", methods=["DELETE"])
    def delete_material(self, id):
        material = request.env["keda.material"].sudo().browse(id)
        if not material.exists():
            return {"status": 404, "message": "Material not found"}
        material.unlink()
        return {"status": 200, "message": "Material deleted"}