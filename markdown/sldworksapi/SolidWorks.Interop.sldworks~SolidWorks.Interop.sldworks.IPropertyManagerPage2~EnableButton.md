---
title: "EnableButton Method (IPropertyManagerPage2)"
project: "SOLIDWORKS API Help"
interface: "IPropertyManagerPage2"
member: "EnableButton"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~EnableButton.html"
---

# EnableButton Method (IPropertyManagerPage2)

Sets whether to enable the buttons on the PropertyManager.

## Syntax

### Visual Basic (Declaration)

```vb
Function EnableButton( _
   ByVal WhichOne As System.Integer, _
   ByVal Enable As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPropertyManagerPage2
Dim WhichOne As System.Integer
Dim Enable As System.Boolean
Dim value As System.Boolean

value = instance.EnableButton(WhichOne, Enable)
```

### C#

```csharp
System.bool EnableButton(
   System.int WhichOne,
   System.bool Enable
)
```

### C++/CLI

```cpp
System.bool EnableButton(
   System.int WhichOne,
   System.bool Enable
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WhichOne`: Button as defined in [swPropertyManagerPageButtons e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPropertyManagerPageButtons_e.html)
- `Enable`: True enables the button, false disables it

### Return Value

True if the button was enabled or disabled, false if not

## VBA Syntax

See [PropertyManagerPage2::EnableButton](ms-its:sldworksapivb6.chm::/sldworks~PropertyManagerPage2~EnableButton.html).

## Remarks

You can only call this method after the page is displayed.

By default, all of the specified buttons that appear at the top of the PropertyManager are initially enabled, except for the Previous Page button.

**NOTE:** The intended use of this method is to disable the Previous Page button when the first of multiple pages is displayed and to disable the Next Page button when the last of multiple pages is displayed. However, you can use it whenever you want.

## See Also

[IPropertyManagerPage2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2.html)
[IPropertyManagerPage2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2_members.html)
[IPropertyManagerPageButton Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageButton.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
