---
title: "Get3DExperienceModelType Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "Get3DExperienceModelType"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~Get3DExperienceModelType.html"
---

# Get3DExperienceModelType Method (IModelDocExtension)

Gets the type of **3D**EXPERIENCE application that owns this model.

## Syntax

### Visual Basic (Declaration)

```vb
Function Get3DExperienceModelType() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As System.Integer

value = instance.Get3DExperienceModelType()
```

### C#

```csharp
System.int Get3DExperienceModelType()
```

### C++/CLI

```cpp
System.int Get3DExperienceModelType();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Type of **3D**EXPERIENCE owner as defined by [sw3DExperienceModelType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.sw3DExperienceModelType_e.html)

## VBA Syntax

See [ModelDocExtension::Get3DExperienceModelType](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~Get3DExperienceModelType.html).

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
