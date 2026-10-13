---
title: "Select2 Method (ISilhouetteEdge)"
project: "SOLIDWORKS API Help"
interface: "ISilhouetteEdge"
member: "Select2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISilhouetteEdge~Select2.html"
---

# Select2 Method (ISilhouetteEdge)

Selects the silhouette edge in the active drawing view.

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
Dim instance As ISilhouetteEdge
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

- `Append`: True appends this selection to the selection list, false replaces the selection list with this selection
- `Data`: [SelectData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectData.html) object

### Return Value

True if the selection is successful, false if not

## VBA Syntax

See [SilhouetteEdge::Select2](ms-its:sldworksapivb6.chm::/Sldworks~SilhouetteEdge~Select2.html).

## Examples

[Select Silhouette Edge Attached to Note (C#)](Select_Silhouette_Edge_Attached_to_Note_Example_CSharp.htm)
[Select Silhouette Edge Attached to Note (VB.NET)](Select_Silhouette_Edge_Attached_to_Note_Example_VBNET.htm)
[Select Silhouette Edge Attached to Note (VBA)](Select_Silhouette_Edge_Attached_to_Note_Example_VB.htm)

## See Also

[ISilhouetteEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISilhouetteEdge.html)
[ISilhouetteEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISilhouetteEdge_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
