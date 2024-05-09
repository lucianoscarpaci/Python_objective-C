from rubicon.objc import objc_method, ObjCClass, send_super, ObjCInstance

ObjCClass.auto_rename = True

NSOperation = ObjCClass("NSOperation")
NSOperationQueue = ObjCClass("NSOperationQueue")
UIApplication = ObjCClass('UIApplication')
UIColor = ObjCClass('UIColor')
UIViewController = ObjCClass('UIViewController')
UIAlertController = ObjCClass('UIAlertController')
UIAlertAction = ObjCClass('UIAlertAction')


class MyViewController(UIViewController):

    @objc_method
    def viewDidLoad(self):
        send_super(__class__, self, "viewDidLoad")
        self.view.backgroundColor = UIColor.blackColor
        print("View")
        # Create and present a UIAlertController after a delay
        # the 500 argument is whats preventing the app from crashing
        self.performSelector_withObject_afterDelay_(
            'presentAlert', None, 500.0)

    @objc_method
    def presentAlert(self):
        alert_controller = UIAlertController.alertControllerWithTitle_message_preferredStyle_(
            'Ask Bot', 'Enter your prompt to the AI: 🤖💬', 1)
        print("Alert")
        # Add a text field for user input
        alert_controller.addTextFieldWithConfigurationHandler_(None)

        
        def _result_handler(action: ObjCInstance) -> None:
            print("User entered prompt")

        action = UIAlertAction.actionWithTitle_style_handler_(
            'OK', 0, _result_handler)
        alert_controller.addAction(action)
        self.presentViewController_animated_completion_(
            alert_controller, True, None)


class MainOperation(NSOperation):

    @objc_method
    def main(self):
        send_super(__class__, self, "main")
        app = UIApplication.sharedApplication
        rootVC = app.keyWindow.rootViewController

        mainVC = MyViewController.new().autorelease()
        rootVC.presentViewController_animated_completion_(
            mainVC, True, None)  # Present the mainVC first

        while childVC := rootVC.presentedViewController:
            rootVC = childVC

        # After presenting mainVC, check if there is a presented view controller and dismiss it
        rootVC.presentAlert()


if __name__ == "__main__":
    operation = MainOperation.new()
    queue = NSOperationQueue.mainQueue
    queue.addOperation(operation)
    queue.waitUntilAllOperationsAreFinished()
