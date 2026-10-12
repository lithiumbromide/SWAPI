---
title: "Close Method (IPropertyManagerPage2)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPage2"
member: "Close"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~Close.html"
---

# Close Method (IPropertyManagerPage2)

Closes the current page in the PropertyManager.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Close( _
   ByVal Okay As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2
Dim Okay As System.Boolean

instance.Close(Okay)
```

### C#

```csharp
void Close(
   System.bool Okay
)
```

### C++/CLI

```cpp
void Close(
   System.bool Okay
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Okay`: VARIANT_True or VARIANT_false

### Return Value

| When you call... | Then... |
| --- | --- |
| Close(VARIANT_True) | IPropertyManagerPage2Handler8::OnClose is called with argument swPropertyManagerPageClose_Okay, regardless of which buttons are displayed at the top of the page. |
| Close(VARIANT_false) | IPropertyManagerPage2Handler8::OnClose is called with argument swPropertyManagerPageClose_Cancel, regardless of which buttons are displayed at the top of the page. |

## VBA Syntax

See [PropertyManagerPage2::Close](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPage2~Close.html).

## See Also

[IPropertyManagerPage2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.html)
[IPropertyManagerPage2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2_members.html)
[IPropertyManagerPage2::Show2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~Show2.html)
[IPropertyManagerPage2::AddControl Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~AddControl.html)
[IPropertyManagerPage2::AddGroupBox Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~AddGroupBox.html)
[IPropertyManagerPage2::SetTitleBitmap2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~SetTitleBitmap2.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
