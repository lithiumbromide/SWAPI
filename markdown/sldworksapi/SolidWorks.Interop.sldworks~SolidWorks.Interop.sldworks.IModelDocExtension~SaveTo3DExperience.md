---
title: "SaveTo3DExperience Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "SaveTo3DExperience"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SaveTo3DExperience.html"
---

# SaveTo3DExperience Method (IModelDocExtension)

Saves this document in [SOLIDWORKS Design connected to the 3DEXPERIENCE platform](ms-its:sldworksapiprogguide.chm:://Overview/SOLIDWORKS_Connected.htm) using the specified save options.

## Syntax

### Visual Basic (Declaration)

```vb
Function SaveTo3DExperience( _
   ByVal Options As System.Object, _
   ByRef Errors As System.Integer, _
   ByRef Warnings As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim Options As System.Object
Dim Errors As System.Integer
Dim Warnings As System.Integer
Dim value As System.Boolean

value = instance.SaveTo3DExperience(Options, Errors, Warnings)
```

### C#

```csharp
System.bool SaveTo3DExperience(
   System.object Options,
   out System.int Errors,
   out System.int Warnings
)
```

### C++/CLI

```cpp
System.bool SaveTo3DExperience(
   System.Object^ Options,
   [Out] System.int Errors,
   [Out] System.int Warnings
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Options`: [ISaveTo3DExperienceOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISaveTo3DExperienceOptions.html) (see **Remarks**)
- `Errors`: Error codes
- `Warnings`: Warning codes

### Return Value

True if the document saved successfully, false if not

## VBA Syntax

See [ModelDocExtension::SaveTo3DExperience](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~SaveTo3DExperience.html).

## Remarks

If the file is:

- new and the file name is specified in Options, then this method acts like **File > Save**. If any other options are specified, then this method acts like **File > Save With Options**.
- already saved to the platform and a new file name is specified in Options, then this method acts like **File > Save As New**.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

## Availability

SOLIDWORKS 2020 SP3.1, Revision Number 28.3.1
