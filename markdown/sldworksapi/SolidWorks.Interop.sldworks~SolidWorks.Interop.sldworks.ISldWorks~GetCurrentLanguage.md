---
title: "GetCurrentLanguage Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetCurrentLanguage"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetCurrentLanguage.html"
---

# GetCurrentLanguage Method (ISldWorks)

Gets the current language used by SOLIDWORKS Design.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCurrentLanguage() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim value As System.String

value = instance.GetCurrentLanguage()
```

### C#

```csharp
System.string GetCurrentLanguage()
```

### C++/CLI

```cpp
System.String^ GetCurrentLanguage();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Current language

## VBA Syntax

See [SldWorks::GetCurrentLanguage](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetCurrentLanguage.html).

## Examples

[Get Language and Localized Menu Names (VBA)](Get_Language_and_Localized_Menu_Names_Example_VB.htm)

## Remarks

Possible return values are:

| chinese chinese-simplified czech english french | german italian japanese korean polish | portuguese-brazilian russian spanish turkish |
| --- | --- | --- |

You can see the current language in use by the SOLIDWORKS Design application in the SOLIDWORKS Design resources (dialogs, menus, and so on).

You can use the return value to set your local resource usage.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)

## Availability

SOLIDWORKS 99, datecode 1999207
