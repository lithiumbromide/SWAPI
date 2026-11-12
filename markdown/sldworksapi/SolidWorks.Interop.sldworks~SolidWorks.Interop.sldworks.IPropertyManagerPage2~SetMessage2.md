---
title: "SetMessage2 Method (IPropertyManagerPage2)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPage2"
member: "SetMessage2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~SetMessage2.html"
---

# SetMessage2 Method (IPropertyManagerPage2)

Obsolete. Superseded by [PropertyManagerPage2::SetMessage3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IPropertyManagerPage2~SetMessage3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function SetMessage2( _
   ByVal Message As System.String, _
   ByVal Visibility As System.Integer, _
   ByVal Caption As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2
Dim Message As System.String
Dim Visibility As System.Integer
Dim Caption As System.String
Dim value As System.Boolean

value = instance.SetMessage2(Message, Visibility, Caption)
```

### C#

```csharp
System.bool SetMessage2(
   System.string Message,
   System.int Visibility,
   System.string Caption
)
```

### C++/CLI

```cpp
System.bool SetMessage2(
   System.String^ Message,
   System.int Visibility,
   System.String^ Caption
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Message`: Message text
- `Visibility`: Visibility state of this message as defined by [swPropertyManagerPageMessageVisibility](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPropertyManagerPageMessageVisibility.html)
- `Caption`: Caption for message

### Return Value

True if the message is set, false if not

## VBA Syntax

See [PropertyManagerPage2::SetMessage2](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPage2~SetMessage2.html).

## Remarks

If Caption is empty, then the current caption is not changed.

This method should be useful when creating multi-page PropertyManager pages where you want different informational messages on each page.

## See Also

[IPropertyManagerPage2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.html)
[IPropertyManagerPage2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
