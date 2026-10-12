---
title: "Select Method (IFacet)"
project: "SOLIDWORKS API Help"
interface: "IFacet"
member: "Select"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFacet~Select.html"
---

# Select Method (IFacet)

Selects the specified facet.

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
Dim instance As IFacet
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

- `Append`: True to append this selection to the selection list, false to replace the selection list with this selection
- `Data`: Pointer to the [ISelectData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectData.html) object

### Return Value

True if the facet is selected, false if not

## VBA Syntax

See [Facet::Select](ms-its:sldworksapivb6.chm::/sldworks~Facet~Select.html).

## Examples

See the [IFacet](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFacet.html) examples.

## See Also

[IFacet Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFacet.html)
[IFacet Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFacet_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
