
import view
import model
import controller


class mvc:
        view = view.view()
        model = model.model()
        controller = controller.controller(view, model)

if __name__ == "__main__":
    main().run()
