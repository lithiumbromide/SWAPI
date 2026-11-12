---
title: "Select Method (IDetailCircle)"
project: "SOLIDWORKS API Help"
interface: "IDetailCircle"
member: "Select"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle~Select.html"
---

# Select Method (IDetailCircle)

Selects the detail circle.

## Syntax

### Visual Basic (Declaration)

```vb
Function Select( _
   ByVal Append As System.Boolean, _
   ByVal Data As SelectData _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDetailCircle
Dim Append As System.Boolean
Dim Data As SelectData
Dim value As System.Boolean

value = instance.Select(Append, Data)
```

### C#

```csharp
System.bool Select(
   System.bool Append,
   SelectData Data
)
```

### C++/CLI

```cpp
System.bool Select(
   System.bool Append,
   SelectData^ Data
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Append`: True appends the detail circle to the selection list, false replaces the selection
  list with this detail circle
- `Data`: Pointer to the [ISelectData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectData.html) object

### Return Value

True if the detail circle is selected, false if not

## VBA Syntax

See [DetailCircle::Select](ms-its:sldworksapivb6.chm::/sldworks~DetailCircle~Select.html).

## Examples

[Create Detail Circle and Detail View (C#)](Create_Detail_Circle_and_Detail_View_Example_CSharp.htm)
[Create Detail Circle and Detail View (VB.NET)](Create_Detail_Circle_and_Detail_View_Example_VBNET.htm)
[Create Detail Circle and Detail View (VBA)](Create_Detail_Circle_and_Detail_View_Example_VB.htm)

## See Also

[IDetailCircle Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle.html)
[IDetailCircle Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDetailCircle_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13.0
