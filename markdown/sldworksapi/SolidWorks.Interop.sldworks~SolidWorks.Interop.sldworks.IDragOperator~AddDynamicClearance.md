---
title: "AddDynamicClearance Method (IDragOperator)"
project: "SOLIDWORKS API Help"
interface: "IDragOperator"
member: "AddDynamicClearance"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~AddDynamicClearance.html"
---

# AddDynamicClearance Method (IDragOperator)

Adds a dynamic clearance detector.

## Syntax

### Visual Basic (Declaration)

```vb
Function AddDynamicClearance( _
   ByVal Comp1 As System.Object, _
   ByVal Comp2 As System.Object, _
   ByVal Value As System.Double, _
   ByVal AppendFlag As System.Boolean, _
   ByVal ShowDim As System.Boolean _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDragOperator
Dim Comp1 As System.Object
Dim Comp2 As System.Object
Dim Value As System.Double
Dim AppendFlag As System.Boolean
Dim ShowDim As System.Boolean
Dim value As System.Integer

value = instance.AddDynamicClearance(Comp1, Comp2, Value, AppendFlag, ShowDim)
```

### C#

```csharp
System.int AddDynamicClearance(
   System.object Comp1,
   System.object Comp2,
   System.double Value,
   System.bool AppendFlag,
   System.bool ShowDim
)
```

### C++/CLI

```cpp
System.int AddDynamicClearance(
   System.Object^ Comp1,
   System.Object^ Comp2,
   System.double Value,
   System.bool AppendFlag,
   System.bool ShowDim
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Comp1`: First component of the clearance pair
- `Comp2`: Second component of the clearance pair
- `Value`: Minimum clearance distance
- `AppendFlag`: True appends the component to the list, false overwrites the list
- `ShowDim`: True displays a dynamic reference dimension of the minimum clearance distance

### Return Value

Newly added clearance pair

## VBA Syntax

See [DragOperator::AddDynamicClearance](ms-its:sldworksapivb6.chm::/sldworks~DragOperator~AddDynamicClearance.html).

## See Also

[IDragOperator Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator.html)
[IDragOperator Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator_members.html)
[IDragOperator::IAddDynamicClearance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~IAddDynamicClearance.html)
[IDragOperator::DynamicClearanceEnabled Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDragOperator~DynamicClearanceEnabled.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
