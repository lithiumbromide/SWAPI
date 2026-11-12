---
title: "SetProgId Method (IMacroFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMacroFeatureData"
member: "SetProgId"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~SetProgId.html"
---

# SetProgId Method (IMacroFeatureData)

Sets the version-independent program ID that is valid for this COM feature.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetProgId( _
   ByVal ProgId As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IMacroFeatureData
Dim ProgId As System.String

instance.SetProgId(ProgId)
```

### C#

```csharp
void SetProgId(
   System.string ProgId
)
```

### C++/CLI

```cpp
void SetProgId(
   System.String^ ProgId
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ProgId`: Name of the program ID for the component that implements the COM feature handler

## VBA Syntax

See [MacroFeatureData::SetProgId](ms-its:sldworksapivb6.chm::/sldworks~MacroFeatureData~SetProgId.html).

## Remarks

See [Exposed COM DLL or Executable and Macro Features](sldworksapiprogguide.chm::/Macro_Features/Exposed_COM_DLL_or_Executable.htm) for details about macro features that define their behavior using COM.

## See Also

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.html)
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.html)
[IMacroFeatureData::GetProgId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~GetProgId.html)
[IMacroFeatureData::IsCOMFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IsCOMFeature.html)

## Availability

SOLIDWORKS 2006 SP4, Revision Number 14.4
