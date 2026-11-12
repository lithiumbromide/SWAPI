---
title: "Select Method (ICenterMark)"
project: "SOLIDWORKS API Help"
interface: "ICenterMark"
member: "Select"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark~Select.html"
---

# Select Method (ICenterMark)

Selects the center mark.

## Syntax

### Visual Basic (Declaration)

```vb
Function Select( _
   ByVal Append As System.Boolean, _
   ByVal Data As System.Object _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ICenterMark
Dim Append As System.Boolean
Dim Data As System.Object
Dim value As System.Boolean

value = instance.Select(Append, Data)
```

### C#

```csharp
System.bool Select(
   System.bool Append,
   System.object Data
)
```

### C++/CLI

```cpp
System.bool Select(
   System.bool Append,
   System.Object^ Data
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Append`: True appends the center mark to the selection list, false replaces the selection list with this center mark
- `Data`: [SelectData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData.html) object

### Return Value

True if the center mark is selected, false if not

## VBA Syntax

See [CenterMark::Select](ms-its:sldworksapivb6.chm::/sldworks~CenterMark~Select.html).

## See Also

[ICenterMark Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark.html)
[ICenterMark Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICenterMark_members.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
