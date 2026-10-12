---
title: "Select4 Method (ISketchHatch)"
project: "SOLIDWORKS API Help"
interface: "ISketchHatch"
member: "Select4"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch~Select4.html"
---

# Select4 Method (ISketchHatch)

Selects the sketch hatch and marks it.

## Syntax

### Visual Basic (Declaration)

```vb
Function Select4( _
   ByVal Append As System.Boolean, _
   ByVal Data As SelectData _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchHatch
Dim Append As System.Boolean
Dim Data As SelectData
Dim value As System.Boolean

value = instance.Select4(Append, Data)
```

### C#

```csharp
System.bool Select4(
   System.bool Append,
   SelectData Data
)
```

### C++/CLI

```cpp
System.bool Select4(
   System.bool Append,
   SelectData^ Data
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Append`: True appends the selection to the selection list, false replaces the selection list with this selection
- `Data`: [ISelectData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectData.html) object

### Return Value

True if the sketch hatch is selected, false if not

## VBA Syntax

See [SketchHatch::Select4](ms-its:sldworksapivb6.chm::/sldworks~SketchHatch~Select4.html).

## See Also

[ISketchHatch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch.html)
[ISketchHatch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch_members.html)
[ISketchHatch::DeSelect Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchHatch~DeSelect.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
