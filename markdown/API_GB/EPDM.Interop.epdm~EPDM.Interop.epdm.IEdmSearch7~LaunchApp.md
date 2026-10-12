---
title: "LaunchApp Method (IEdmSearch7)"
project: "SOLIDWORKS PDM Professional API Help"
interface: "IEdmSearch7"
member: "LaunchApp"
kind: "method"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch7~LaunchApp.html"
---

# LaunchApp Method (IEdmSearch7)

Starts the search tool application.

## Syntax

### Visual Basic

```vb
Sub LaunchApp( _
   ByVal hParentWnd As System.Integer, _
   Optional ByVal bsDefault As System.String, _
   Optional ByVal oStartFolderPathOrID As System.Object, _
   Optional ByVal lEdmLaunchSearchFlags As System.Integer _
)
```

### C#

```csharp
void LaunchApp(
   System.int hParentWnd,
   System.string bsDefault,
   System.object oStartFolderPathOrID,
   System.int lEdmLaunchSearchFlags
)
```

### C++/CLI

```cpp
void LaunchApp(
   System.int hParentWnd,
   System.String^ bsDefault,
   System.Object^ oStartFolderPathOrID,
   System.int lEdmLaunchSearchFlags
)
```

### Parameters

- `hParentWnd`: Parent window handle
- `bsDefault`: Name of a search form; name of a search favorite if lEdmLaunchSearchFlags contains [EdmLaunchSearchFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmLaunchSearchFlags.html).Elsf_DefaultIsAFavorite
- `oStartFolderPathOrID`: Path or ID of the folder in which the search tool should start looking
- `lEdmLaunchSearchFlags`: Combination of [EdmLaunchSearchFlags](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmLaunchSearchFlags.html) bits

## Remarks

[Return codes:](ReturnCodes.htm)

- S_OK: The method successfully executed.

## See Also

[IEdmSearch7 Interface](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch7.html)
[IEdmSearch7 Members](EPDM.Interop.epdm~EPDM.Interop.epdm.IEdmSearch7_members.html)

## Availability

SOLIDWORKS PDM Professional 2009
