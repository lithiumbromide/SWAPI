---
title: "GetControl Method (IPropertyManagerPageActiveX)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPageActiveX"
member: "GetControl"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageActiveX~GetControl.html"
---

# GetControl Method (IPropertyManagerPageActiveX)

Gets the interface to this ActiveX control.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetControl() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPageActiveX
Dim value As System.Object

value = instance.GetControl()
```

### C#

```csharp
System.object GetControl()
```

### C++/CLI

```cpp
System.Object^ GetControl();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

ActiveX control

## VBA Syntax

See [PropertyManagerPageActiveX::GetControl](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPageActiveX~GetControl.html).

## Remarks

Do not call this method until the PropertyManager page is displayed. If you call this method before the PropertyManager page is displayed, then the method will fails and retval is NULL.

When the ActiveX control is created, the program creating the PropertyManager page should receive notification from the IPropertyManagerPage2Handler5::OnActiveXControlCreated method. Your program should not call IPropertyManagerPageActiveX::GetControl or [IPropertyManagerPageActiveX::IGetControl](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPageActiveX~IGetControl.html) to get the interface object for this ActiveX control, because the PropertyManager page is not displayed when this notification is sent.

When the page is displayed, your program can now initialize the control properties so that the control looks how you want it to appear when it the PropertyManager page is initially displayed. You can set up the event sink for the control so that you receive notification when certain events happen to the control.

## See Also

[IPropertyManagerPageActiveX Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageActiveX.html)
[IPropertyManagerPageActiveX Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageActiveX_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
