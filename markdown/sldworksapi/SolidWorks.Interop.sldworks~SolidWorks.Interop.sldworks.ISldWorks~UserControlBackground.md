---
title: "UserControlBackground Property (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "UserControlBackground"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~UserControlBackground.html"
---

# UserControlBackground Property (ISldWorks)

Gets and sets whether the user has control over the application.

## Syntax

### Visual Basic (Declaration)

```vb
Property UserControlBackground As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim value As System.Boolean

instance.UserControlBackground = value

value = instance.UserControlBackground
```

### C#

```csharp
System.bool UserControlBackground {get; set;}
```

### C++/CLI

```cpp
property System.bool UserControlBackground {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the user has control over the application, false if not (see Remarks)

## VBA Syntax

See [SldWorks::UserControlBackground](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~UserControlBackground.html).

## Remarks

Setting this property to true causes the SOLIDWORKS Design application to run in the background and not be visible. Use [ISldWorks::UserControl](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~UserControl.html) if you want to run the SOLIDWORKS Design application in the foreground and be visible.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::UserControl Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~UserControl.html)
[ISldWorks::Visible Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~Visible.html)
[IFrame::KeepInvisible Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFrame~KeepInvisible.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
