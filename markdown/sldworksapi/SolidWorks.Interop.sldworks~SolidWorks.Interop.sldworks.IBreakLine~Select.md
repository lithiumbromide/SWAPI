---
title: "Select Method (IBreakLine)"
project: "SOLIDWORKS API Help"
interface: "IBreakLine"
member: "Select"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine~Select.html"
---

# Select Method (IBreakLine)

Selects the break line and marks it.

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
Dim instance As IBreakLine
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

- `Append`: True appends the break line to the selection list, false replaces the selection list with this break line
- `Data`: Pointer to the [ISelectData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectData.html) object

### Return Value

True if the selection is successful, false if not

## VBA Syntax

See [BreakLine::Select](ms-its:sldworksapivb6.chm::/sldworks~BreakLine~Select.html).

## Examples

[Create Break View (C#)](Create_Broken_View_Example_CSharp.htm)
[Create Break View (V.NET)](Create_Broken_View_Example_VBNET.htm)
[Create Break View (VBA)](Create_Broken_View_Example_VB.htm)

## See Also

[IBreakLine Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine.html)
[IBreakLine Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBreakLine_members.html)

## Availability

SOLIDWORKS 2005 FCS, Revision Number 13
