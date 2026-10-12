---
title: "Select2 Method (IBody2)"
project: "SOLIDWORKS API Help"
interface: "IBody2"
member: "Select2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Select2.html"
---

# Select2 Method (IBody2)

Selects this body and marks it.

## Syntax

### Visual Basic (Declaration)

```vb
Function Select2( _
   ByVal Append As System.Boolean, _
   ByVal Data As SelectData _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IBody2
Dim Append As System.Boolean
Dim Data As SelectData
Dim value As System.Boolean

value = instance.Select2(Append, Data)
```

### C#

```csharp
System.bool Select2(
   System.bool Append,
   SelectData Data
)
```

### C++/CLI

```cpp
System.bool Select2(
   System.bool Append,
   SelectData^ Data
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Append`: True appends the selection list, false replaces the selection list
- `Data`: Pointer to the [ISelectData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectData.html) object

### Return Value

True if the body was selected, false if not

## VBA Syntax

See [Body2::Select2](ms-its:sldworksapivb6.chm::/sldworks~Body2~Select2.html).

## Examples

[Move Bodies (C#)](Move_Bodies_Example_CSharp.htm)
[Move Bodies (VB.NET)](Move_Bodies_Example_VBNET.htm)
[Move Bodies (VBA)](Move_Bodies_Example_VB.htm)

## See Also

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.html)
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15
