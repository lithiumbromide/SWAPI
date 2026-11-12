---
title: "SelectComponentsBySize Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "SelectComponentsBySize"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~SelectComponentsBySize.html"
---

# SelectComponentsBySize Method (IAssemblyDoc)

Selects assembly components by percent of assembly size.

## Syntax

### Visual Basic (Declaration)

```vb
Function SelectComponentsBySize( _
   ByVal Percent As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim Percent As System.Double
Dim value As System.Boolean

value = instance.SelectComponentsBySize(Percent)
```

### C#

```csharp
System.bool SelectComponentsBySize(
   System.double Percent
)
```

### C++/CLI

```cpp
System.bool SelectComponentsBySize(
   System.double Percent
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Percent`: 0.0 <= Percent of assembly size <= 100.0

### Return Value

True if Percent is valid, false if Percent > 100 or Percent < 0

## VBA Syntax

See [AssemblyDoc::SelectComponentsBySize](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~SelectComponentsBySize.html).

## Examples

[Select Assembly Components by Size (VBA)](Select_Assembly_Components_by_Size_Example_VB.htm)
[Select Assembly Components by Size (VB.NET)](Select_Assembly_Components_by_Size_Example_VBNET.htm)
[Select Assembly Components by Size (C#)](Select_Assembly_Components_by_Size_Example_CSharp.htm)

## Remarks

This method corresponds to **Tools > Component Selection > Select By Size**.

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)
[IModelDocExtension::SelectByID2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.html)
[IModelDocExtension::SelectAll Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectAll.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
