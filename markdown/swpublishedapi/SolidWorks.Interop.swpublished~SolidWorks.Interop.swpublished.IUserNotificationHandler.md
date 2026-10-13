---
title: "IUserNotificationHandler Interface"
project: "SOLIDWORKS Custom Interfaces API Help"
interface: "IUserNotificationHandler"
member: ""
kind: "interface"
source: "swpublishedapi/SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IUserNotificationHandler.html"
---

# IUserNotificationHandler Interface

Must be implemented by the add-in application to handle callbacks from [IUserNotificationDefinition](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IUserNotificationDefinition.html).

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IUserNotificationHandler
```

### Visual Basic (Usage)

```vb
Dim instance As IUserNotificationHandler
```

### C#

```csharp
public interface IUserNotificationHandler
```

### C++/CLI

```cpp
public interface class IUserNotificationHandler
```

## VBA Syntax

See [UserNotificationHandler](ms-its:swpublishedapivb6.chm::/swpublished~UserNotificationHandler.html).

## Examples

To create a SOLIDWORKS .NET add-in that implements this interface:

1. Open a new project in Visual Studio using SOLIDWORKS template, **Visual C# - SwCSharpAddin**.
2. Add **CNotification_A_Handler.cs** with the following code to the add-in to handle user notifications:

  using System;

  using System.Collections.Generic;

  using System.Linq;

  using System.Text;

  using System.Runtime.InteropServices;

  using SolidWorks.Interop.sldworks;

  using SolidWorks.Interop.swpublished;

  using System.Diagnostics;

  namespace `addin_name`

  {

  public class CNotification_A_Handler : IUserNotificationHandler

  {

  // The add-in author needs to decide how the handler should react to user responses

  // In this example, pass the SOLIDWORKS application object and the target model into the handler's constructor for later use

  // Model can be null here since notifications can relate to the application, rather than the document

  private ISldWorks iswApp;

  private ModelDoc2 iswModelDoc;

  public CNotification_A_Handler(ISldWorks swApp, ModelDoc2 swModelDoc)

  {

  iswApp = swApp;

  iswModelDoc = swModelDoc;

  }

  public void OnTimeout()

  {

  Debug.Print("CNotification_A_Handler::OnTimeout");

  // To Do: Implement desired response

  }

  public void OnUserClose()

  {

  Debug.Print("CNotification_A_Handler::OnUserClose");

  // To Do: Implement desired response

  }

  public void OnUserResponseA(bool DoNotShowAgain)

  {

  Debug.Print(String.Format("CNotification_A_Handler::OnUserResponseA, Don't Show Again? == {0}", DoNotShowAgain));

  // To Do: Implement desired response

  }

  public void OnUserResponseB(bool DoNotShowAgain)

  {

  Debug.Print(String.Format("CNotification_A_Handler::OnUserResponseB, Don't Show Again? == {0}", DoNotShowAgain));

  // To Do: Implement desired response

  }

  }

  }
3. Add a ShowNotification() function to the UI Callbacks region in **SwAddin.cs** to declare and define a user notification and create the user notification handler:

  ```
  public class SwAddin : ISwAddin
  {
      ...
      private const String NotifyID_A = "MyAddInName+Notification_A";
      private IUserNotificationDefinition NotifyDefn_A;
  ```

  ```
      void ShowNotification()
      {
          // This unique user notification is triggered from the command bar.
          // Have we already defined this user notification in this session? If so, reuse it.
          if (NotifyDefn_A == null)
          {
              // Create a new notification definition
              NotifyDefn_A = swApp.DefineUserNotification(NotifyID_A) As IUserNotificationDefinition;
              // Configure the notification definition
              NotifyDefn_A.Severity = (int) swUserNotificationSeverity_e.swUserNotificationSeverity_Warning;
              NotifyDefn_A.Title = "Notification from my add-in";
              NotifyDefn_A.Message = "Something important happened that you should know about.";
              NotifyDefn_A.ResponseAType = (int) swUserNotificationResponseType_e.swUserNotificationResponseType_Button;
              NotifyDefn_A.ResponseAText = "OK";
              // ResponseBType & ResponseBText have default values: swUserNotificationResponseType_None & ""
              // IncludeDoNotShowAgain has default value: VARIANT_TRUE
          }
  ```

  ```
          ModelDoc2 swModelDoc = swApp.ActiveDoc;
  ```

  ```
          // Create a handler for this instance of the user notification;
          // In this example, the handler will go out of scope here
          // SOLIDWORKS will retain its pointer to the handler object until the notification has been dismissed and the response callback has been called.
          CNotification_A_Handler myHandler =  new CNotification_A_Handler(swApp, swModelDoc);

          // Show the user notification for the application
  ```

  ```
          String strTarget = "";
  ```

  ```
          swShowNotificationResult_e notifyResult;

          if (swModelDoc != null)

          {

              strTarget = "IModelDocExtension";

              notifyResult = (swShowNotificationResult_e)swModelDoc.Extension.ShowUserNotification(NotifyDefn_A, myHandler);

          }

          else

          {

              strTarget = "ISldWorks";

              notifyResult = (swShowNotificationResult_e)swApp.ShowUserNotification(NotifyDefn_A, myHandler);

          }

          switch (notifyResult)
          {
              case swShowNotificationResult_e.swShowNotificationResult_Shown:
                  // The *modeless* notification has been shown
                  break;
              case swShowNotificationResult_e.swShowNotificationResult_DontShowAgain:
                  // The notification was not shown because 'Don't show again' was previously checked
                  break;
              case swShowNotificationResult_e.swShowNotificationResult_FailedInvalidDefinition:
                  // The notification could not be displayed due to an invalid definition (e.g. empty title/description)
                  break;
              case swShowNotificationResult_e.swShowNotificationResult_FailedInvalidHandler:
                  // The notification was not displayed because the Handler argument was NULL or did not support the expected interface
                  break;
              default:
                  // Unknown error
                  break;
          }
      }

  }
  ```
4. Modify the UI Methods region in **SwAddin.cs** to add a command item to the add-in's toolbar:

  cmdIndex0 = cmdGroup.AddCommandItem2("Show Notification", -1, "Show User Notification", "Show User Notification", 0, "ShowNotification", "", mainItemID1, menuToolbarOption);

## See Also

[IUserNotificationHandler Members](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IUserNotificationHandler_members.html)
[SolidWorks.Interop.swpublished Namespace](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished_namespace.html)
[IMessageBarHandler Interface](SolidWorks.Interop.swpublished~SolidWorks.Interop.swpublished.IMessageBarHandler.html)
