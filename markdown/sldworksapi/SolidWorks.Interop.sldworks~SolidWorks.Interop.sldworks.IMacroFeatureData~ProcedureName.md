---
title: "ProcedureName Property (IMacroFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMacroFeatureData"
member: "ProcedureName"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~ProcedureName.html"
---

# ProcedureName Property (IMacroFeatureData)

Gets or sets a name of the procedure in the macro for this macro feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property ProcedureName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IMacroFeatureData
Dim value As System.String

instance.ProcedureName = value

value = instance.ProcedureName
```

### C#

```csharp
System.string ProcedureName {get; set;}
```

### C++/CLI

```cpp
property System.String^ ProcedureName {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Name of the procedure in the macro

## VBA Syntax

See [MacroFeatureData::ProcedureName](ms-its:sldworksapivb6.chm::/sldworks~MacroFeatureData~ProcedureName.html).

## See Also

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.html)
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.html)
[IMacroFeatureData::GetModuleCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetModuleCount.html)
[IMacroFeatureData::GetModuleNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetModuleNames.html)
[IMacroFeatureData::GetProcedureCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetProcedureCount.html)
[IMacroFeatureData::GetProcedureNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetProcedureNames.html)
[IMacroFeatureData::GetPropertyManagerHandleModuleCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetPropertyManagerHandleModuleCount.html)
[IMacroFeatureData::GetPropertyManagerHandleModuleNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetPropertyManagerHandleModuleNames.html)
[IMacroFeatureData::GetPropertyManagerHandleProcedureCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetPropertyManagerHandleProcedureCount.html)
[IMacroFeatureData::GetPropertyManagerHandleProcedureNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetPropertyManagerHandleProcedureNames.html)
[IMacroFeatureData::IGetModuleNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetModuleNames.html)
[IMacroFeatureData::IGetProcedureNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetProcedureNames.html)
[IMacroFeatureData::IGetPropertyManagerHandleModuleNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetPropertyManagerHandleModuleNames.html)
[IMacroFeatureData::IGetPropertyManagerHandleProcedureNames Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetPropertyManagerHandleProcedureNames.html)
[IMacroFeatureData::MacroFileName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~MacroFileName.html)
[IMacroFeatureData::ModuleName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~ModuleName.html)
[IMacroFeatureData::PropertyManagerHandleMacroFileName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~PropertyManagerHandleMacroFileName.html)
[IMacroFeatureData::PropertyManagerHandleModuleName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~PropertyManagerHandleModuleName.html)
[IMacroFeatureData::PropertyManagerHandleProcedureName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~PropertyManagerHandleProcedureName.html)
[IMacroFeatureData::SecurityHandleMacroFileName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SecurityHandleMacroFileName.html)
[IMacroFeatureData::SecurityHandleModuleName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SecurityHandleModuleName.html)
[IMacroFeatureData::SecurityHandleProcedureName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SecurityHandleProcedureName.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
