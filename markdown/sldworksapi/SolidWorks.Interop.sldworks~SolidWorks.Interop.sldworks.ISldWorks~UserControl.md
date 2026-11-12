---
title: "UserControl Property (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "UserControl"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~UserControl.html"
---

# UserControl Property (ISldWorks)

Gets and sets whether the user has control over the application.

## Syntax

### Visual Basic (Declaration)

```vb
Property UserControl As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim value As System.Boolean

instance.UserControl = value

value = instance.UserControl
```

### C#

```csharp
System.bool UserControl {get; set;}
```

### C++/CLI

```cpp
property System.bool UserControl {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the user has control over the application, false if not (see **Remarks**)

## VBA Syntax

See [SldWorks::UserControl](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~UserControl.html).

## Examples

[Run or Attach to SOLIDWORKS (VBA)](SOLIDWORKS_Visible_or_BackGround_Example_VB.htm)
[Traverse Bodies (C++)](Traverse_Bodies_Example_CPlusPlusCLI.htm)
[Keep SOLIDWORKS Invisible While Activating Documents (C#)](Keep_SOLIDWORKS_Invisible_While_Activating_Documents_Example_CSharp.htm)
[Keep SOLIDWORKS Invisible While Activating Documents (VB.NET)](Keep_SOLIDWORKS_Invisible_While_Activating_Documents_Example_VBNET.htm)
[Keep SOLIDWORKS Invisible While Activating Documents (VBA)](Keep_SOLIDWORKS_Invisible_While_Activating_Documents_Example_VB.htm)
[Get Names of Configurations Using Variant (C++)](ConfigurationTraversalCPP.htm)

## Remarks

If the SOLIDWORKS Design application is started by your program, then the SOLIDWORKS Design application closes when your program ends. However, if you pass control of the SOLIDWORKS Design application to the end-user, then it remains running after your program ends.

Setting this property to true causes the SOLIDWORKS Design application to run in the foreground and be visible. Use [ISldWorks::UserControlBackground](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~UserControlBackground.html) if you want to run the SOLIDWORKS Design application in the background and not be visible.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::CloseDoc Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CloseDoc.html)
[ISldWorks::QuitDoc Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~QuitDoc.html)
[ISldWorks::Visible Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~Visible.html)
[IFrame::KeepInvisible Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~KeepInvisible.html)
