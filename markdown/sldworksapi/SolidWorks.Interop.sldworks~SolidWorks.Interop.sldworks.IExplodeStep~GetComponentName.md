---
title: "GetComponentName Method (IExplodeStep)"
project: "SOLIDWORKS API Help"
interface: "IExplodeStep"
member: "GetComponentName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~GetComponentName.html"
---

# GetComponentName Method (IExplodeStep)

Gets the name of the specified component in this explode step.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetComponentName( _
   ByVal Index As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IExplodeStep
Dim Index As System.Integer
Dim value As System.String

value = instance.GetComponentName(Index)
```

### C#

```csharp
System.string GetComponentName(
   System.int Index
)
```

### C++/CLI

```cpp
System.String^ GetComponentName(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`: Index of the component in this explode step

### Return Value

Name of the component

## VBA Syntax

See [ExplodeStep::GetComponentName](ms-its:sldworksapivb6.chm::/sldworks~ExplodeStep~GetComponentName.html).

## Remarks

Before calling this method, call [IExplodeStep::GetNumOfComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~GetNumOfComponents.html) to get a valid value for Index.

## See Also

[IExplodeStep Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep.html)
[IExplodeStep Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep_members.html)
[IExplodeStep::GetComponents Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExplodeStep~GetComponents.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
