---
title: "MacroFileName Property (IMacroFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMacroFeatureData"
member: "MacroFileName"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~MacroFileName.html"
---

# MacroFileName Property (IMacroFeatureData)

Gets or sets the path and file name for the macro for the macro feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property MacroFileName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IMacroFeatureData
Dim value As System.String

instance.MacroFileName = value

value = instance.MacroFileName
```

### C#

```csharp
System.string MacroFileName {get; set;}
```

### C++/CLI

```cpp
property System.String^ MacroFileName {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Path and file name of the macro

## VBA Syntax

See [MacroFeatureData::MacroFileName](ms-its:sldworksapivb6.chm::/sldworks~MacroFeatureData~MacroFileName.html).

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
[IMacroFeatureData::ModuleName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~ModuleName.html)
[IMacroFeatureData::ProcedureName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~ProcedureName.html)
[IMacroFeatureData::PropertyManagerHandleMacroFileName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~PropertyManagerHandleMacroFileName.html)
[IMacroFeatureData::PropertyManagerHandleModuleName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~PropertyManagerHandleModuleName.html)
[IMacroFeatureData::PropertyManagerHandleProcedureName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~PropertyManagerHandleProcedureName.html)
[IMacroFeatureData::SecurityHandleMacroFileName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SecurityHandleMacroFileName.html)
[IMacroFeatureData::SecurityHandleModuleName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SecurityHandleModuleName.html)
[IMacroFeatureData::SecurityHandleProcedureName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SecurityHandleProcedureName.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
