---
title: "Select Method (ISilhouetteEdge)"
project: "SOLIDWORKS API Help"
interface: "ISilhouetteEdge"
member: "Select"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISilhouetteEdge~Select.html"
---

# Select Method (ISilhouetteEdge)

Obsolete. Superseded by [ISilhouetteEdge::Select2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISilhouetteEdge~Select2.html).

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
Dim instance As ISilhouetteEdge
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

- `Append`: True appends this selection to the selection list, false replaces the selection list with this selection
- `Data`: [SelectData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectData.html) object

### Return Value

True if the selection is successful, false if not

## VBA Syntax

See [SilhouetteEdge::Select](ms-its:sldworksapivb6.chm::/Sldworks~SilhouetteEdge~Select.html).

## See Also

[ISilhouetteEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISilhouetteEdge.html)
[ISilhouetteEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISilhouetteEdge_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
