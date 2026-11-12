---
title: "IsActive Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "IsActive"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IsActive.html"
---

# IsActive Method (IModelDoc2)

Gets whether the specified assembly component is shown or hidden in this model document.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsActive( _
   ByVal CompStr As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim CompStr As System.String
Dim value As System.Boolean

value = instance.IsActive(CompStr)
```

### C#

```csharp
System.bool IsActive(
   System.string CompStr
)
```

### C++/CLI

```cpp
System.bool IsActive(
   System.String^ CompStr
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `CompStr`: Name specification of the component

### Return Value

True if component is shown, false if component is hidden

## VBA Syntax

See [ModelDoc2::IsActive](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~IsActive.html).

## Remarks

The CompStr parameter is the full assembly component name designation. The format of the name designation is:

parentModel/childModel

where:

childModel is the model whose display status you want to determine. For example, if you want to determine the display status of a part named SPOKE.SLDPRT and if this part is a child of WHEEL.SLDPRT, which itself is a child of AXIS.SLDPRT, then you would specify CompStr as follows:

AXIS/WHEEL/SPOKE

TIP: The assembly component name designation is shown in the lower-left corner of the SOLIDWORKS Design application when an assembly component is selected.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::ShowComponent2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ShowComponent2.html)
[IModelDoc2::HideComponent2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~HideComponent2.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
