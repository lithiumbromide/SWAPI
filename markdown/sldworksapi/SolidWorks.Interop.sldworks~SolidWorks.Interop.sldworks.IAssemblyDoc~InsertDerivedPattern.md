---
title: "InsertDerivedPattern Method (IAssemblyDoc)"
project: "SOLIDWORKS API Help"
interface: "IAssemblyDoc"
member: "InsertDerivedPattern"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~InsertDerivedPattern.html"
---

# InsertDerivedPattern Method (IAssemblyDoc)

Obsolete. See [IFeatureManager::CreateFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~CreateFeature.html) and the Remarks in [IDerivedPatternFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDerivedPatternFeatureData.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertDerivedPattern() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAssemblyDoc
Dim value As System.Boolean

value = instance.InsertDerivedPattern()
```

### C#

```csharp
System.bool InsertDerivedPattern()
```

### C++/CLI

```cpp
System.bool InsertDerivedPattern();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the derived component from the selected pattern and seed components is created, false if not

## VBA Syntax

See [AssemblyDoc::InsertDerivedPattern](ms-its:sldworksapivb6.chm::/sldworks~AssemblyDoc~InsertDerivedPattern.html).

## Examples

[Get Number of Instances Skipped in Driving Feature (C#)](Get_Number_of_Instances_Skipped_in_Driving_Feature_Example_CSharp.htm)
[Get Number of Instances Skipped in Driving Feature (VB.NET)](Get_Number_of_Instances_Skipped_in_Driving_Feature_Example_VBNET.htm)
[Get Number of Instances Skipped in Driving Feature (VBA)](Get_Number_of_Instances_Skipped_in_Driving_Feature_Example_VB.htm)

## Remarks

Use [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html) to select the components, which must be ordered:

- seed component = 1
- pattern feature = 6

## See Also

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.html)

## Availability

SOLIDWORKS 2003 SP4, Revision Number 11.4
