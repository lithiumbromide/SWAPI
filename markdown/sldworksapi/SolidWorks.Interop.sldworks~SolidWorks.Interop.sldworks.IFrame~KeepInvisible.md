---
title: "KeepInvisible Property (IFrame)"
project: "SOLIDWORKS API Help"
interface: "IFrame"
member: "KeepInvisible"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~KeepInvisible.html"
---

# KeepInvisible Property (IFrame)

Gets or sets whether to keep the SOLIDWORKS frame invisible.

## Syntax

### Visual Basic (Declaration)

```vb
Property KeepInvisible As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFrame
Dim value As System.Boolean

instance.KeepInvisible = value

value = instance.KeepInvisible
```

### C#

```csharp
System.bool KeepInvisible {get; set;}
```

### C++/CLI

```cpp
property System.bool KeepInvisible {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to keep the SOLIDWORKS frame invisible, false to keep it visible

## VBA Syntax

See [Frame::KeepInvisible](ms-its:sldworksapivb6.chm::/sldworks~Frame~KeepInvisible.html).

## Examples

[Keep SOLIDWORKS Invisible While Activating Documents (C#)](Keep_SOLIDWORKS_Invisible_While_Activating_Documents_Example_CSharp.htm)
[Keep SOLIDWORKS Invisible While Activating Documents (VB.NET)](Keep_SOLIDWORKS_Invisible_While_Activating_Documents_Example_VBNET.htm)
[Keep SOLIDWORKS Invisible While Activating Documents (VBA)](Keep_SOLIDWORKS_Invisible_While_Activating_Documents_Example_VB.htm)

## Remarks

Use this property when SOLIDWORKS is [invisible](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~Visible.html) and you want to [activate](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~ActivateDoc2.html) a component and prevent SOLIDWORKS from becoming visible. Be sure to set this property back to false after the operation for which you set it to true completes.

## See Also

[IFrame Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame.html)
[IFrame Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame_members.html)
[ISldWorks::UserControl Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~UserControl.html)
[ISldWorks::Visible Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~Visible.html)
[ISldWorks::UserControlBackground Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~UserControlBackground.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
