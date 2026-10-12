---
title: "Accessing SOLIDWORKS Add-in Objects"
project: ""
interface: ""
member: ""
kind: "topic"
source: "sldworksapiprogguide/Overview/Accessing_Add-ins.htm"
---

# Accessing SOLIDWORKS Add-in Objects

There are two types of add-ins that you can use with SOLIDWORKS:

- **SOLIDWORKS add-ins,** which provide additional functionality and may be included in SOLIDWORKS Professional or SOLIDWORKS Premium or purchased separately. This topic discusses how to reliably access four SOLIDWORKS add-in objects using [ISldWorks::GetAddInObject](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetAddInObject.html).
- **Other add-ins** developed by you or SOLIDWORKS Partners. See [SOLIDWORKS API Standalone and Add-in Applications Overview](../GettingStarted/SolidWorks_API_Standalone_and_Add-in_Applications_Overview.htm).

To see the SOLIDWORKS add-ins that you are licensed to use, select **Tools > Add-Ins** from the SOLIDWORKS menu. The Add-Ins dialog lists SOLIDWORKS add-ins at the top and Other add-ins at the bottom. To get the functionality of a SOLIDWORKS add-in or to use its APIs, you must load it either from the Add-Ins dialog or programmatically. In the Add-Ins dialog, select the check box next to the add-in of interest and click **OK**. To load the add-in programmatically, call [ISldWorks::LoadAddIn](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~LoadAddIn.html), passing in the add-in name.

### Accessing SOLIDWORKS Add-in Objects

After loading a SOLIDWORKS add-in either through the user interface or by calling ISldWorks::LoadAddIn, in order to use its APIs, you must first access the add-in's API object by calling ISldWorks::GetAddInObject. The following table lists the four SOLIDWORKS add-ins whose add-in objects can be retrieved by calling ISldWorks::GetAddInObject with either a GUID, a version-independent ProgID or, in two cases, a version-specific ProgID:

| Add-in | Version-independent ProgID | Version-specific ProgID (for SW2019) | GUID location in the Windows Registry (regedit.exe)... | Add-in object returned by ISldWorks::GetAddInObject |
| --- | --- | --- | --- | --- |
| FeatureWorks | "FeatureWorks.FeatureWorksApp" | Not applicable - use version-independent ProgID or GUID | HKEY_LOCAL_MACHINE\SOFTWARE\SolidWorks\Applications\FeatureWorks | IFeatureWorksApp |
| SOLIDWORKS Inspection | "Inspection.ExtSwAddin" | Not applicable - use version-independent ProgID or GUID | Search for SOLIDWORKS Inspection in data fields of HKEY_LOCAL_MACHINE\SOFTWARE\SolidWorks\SOLIDWORKS 2022\Addins\ . (The GUID is highlighted in the left panel when the add-in name is found in the right panel.) | IInspectionAddinMgr |
| SOLIDWORKS Design Checker | "SWDesignChecker.SWDesignCheck" | "SWDesignChecker.SWDesignCheck.2019" | Search for SOLIDWORKS Design Checker in data fields of HKEY_LOCAL_MACHINE\SOFTWARE\SolidWorks\SOLIDWORKS 2019\Addins\ . (The GUID is highlighted in the left panel when the add-in name is found in the right panel.) | ISWDesignCheck |
| SOLIDWORKS Simulation | "SldWorks.Simulation" | "SldWorks.Simulation.12" | HKEY_LOCAL_MACHINE\SOFTWARE\SolidWorks\SOLIDWORKS 2019\Applications\SOLIDWORKS Simulation | ICwAddincallback (access ICosmosWorks through ICwAddinCallback::CosmosWorks) |
| SOLIDWORKS Utilities | "Utilities.UtilitiesApp" | Not applicable - use version-independent ProgID or GUID | HKEY_LOCAL_MACHINE\SOFTWARE\SolidWorks\Applications\SOLIDWORKS Utilities | IUtilities |

#### Version-Independent ProgID

The version-independent ProgID of a SOLIDWORKS add-in remains unchanged from one version of SOLIDWORKS to the next.

Some SOLIDWORKS add-ins (e.g., FeatureWorks and SOLIDWORKS Utilities) use only version-independent ProgIDs. As a result, the version-independent ProgID can be used successfully from any version of SOLIDWORKS installed, as long as the add-in, itself, is loaded.

Other SOLIDWORKS add-ins (e.g., SOLIDWORKS Simulation and SOLIDWORKS Design Checker) use either version-specific or version-independent ProgIDs. When you have multiple SOLIDWORKS installations, the version-independent ProgID can only be used successfully from the latest version of SOLIDWORKS. If you have multiple SOLIDWORKS installations and are running one of the earlier versions, passing in the version-independent ProgID results in type mismatches and a failure to access the SOLIDWORKS add-in object. In that case, you must pass in the version-specific ProgID to successfully access the SOLIDWORKS add-in object.

#### Version-Specific ProgID

The version-specific ProgID of a SOLIDWORKS add-in changes from one version of SOLIDWORKS to the next.

When you have multiple SOLIDWORKS installations, for two SOLIDWORKS add-ins (SOLIDWORKS Simulation and SOLIDWORKS Design Checker), passing in the version-specific ProgID succeeds regardless of whether you are running the latest version or an earlier version.

The most reliable method for accessing SOLIDWORKS add-in objects, when you do not have strict control over the installation history of your system, is to first call [ISldWorks::RevisionNumber](sldworksAPI.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~RevisionNumber.html) to identify the version of SOLIDWORKS running and then use that information to calculate at runtime the SOLIDWORKS-compatible version-specific ProgID for the add-in.

The calculation of the version-specific ProgID differs between SOLIDWORKS Simulation and SOLIDWORKS Design Checker. In the calculations below, `SOLIDWORKS_major_version_number` is the leftmost two digits in the string returned by ISldWorks::RevisionNumber. For example, if ISldWorks::RevisionNumber returns "27.0.0", then `SOLIDWORKS_major_version_number` is 27, and the minor version decimal number is 0.0.

###### SOLIDWORKS Simulation Version-Specific ProgID

Specify ProgID as "Sldworks.Simulation.`nn`", where:

- `nn` = `SOLIDWORKS_major_version_number` - 15

###### SOLIDWORKS Design Checker Version-Specific ProgID

Specify ProgID as "SWDesignChecker.SWDesignCheck.`nnnn`", where:

- `nnnn` = `SOLIDWORKS_major_version_number + 1992`

#### GUID

Specify Clsid with a GUID in curly braces, "{GUID}", or ISldWorks::GetAddInObject will interpret it as a ProgID.

#### Code Snippets

The following code snippets demonstrate, in four languages, how to calculate the SOLIDWORKS-compatible version-specific ProgID for the SOLIDWORKS Simulation add-in and use it in ISldWorks::GetAddInObject to retrieve the correct SOLIDWORKS Simulation add-in object.

###### VBA

```vb
Option Explicit
Sub main()
   Dim SwApp As SldWorks.SldWorks
    Dim COSMOSWORKS As Object
    Dim COSMOSObject As Object
    Dim swVersion As Long
    Dim cwVersion As Long
    Dim cwProgID As String
```

...

```vb
   'Connect to SOLIDWORKS
    If SwApp Is Nothing Then Set SwApp = Application.SldWorks

   'Determine host SOLIDWORKS major version
     swVersion  = Left(SwApp.RevisionNumber, 2)

    'Calculate the version-specific ProgID of the Simulation add-in that is compatible with this version of SOLIDWORKS
     cwVersion  =  swVersion  -  15
     cwProgID  =  "SldWorks.Simulation." & cwVersion
     Debug.Print (cwProgID)

    'Get the SOLIDWORKS Simulation object
    Set COSMOSObject = SwApp.GetAddInObject(cwProgID)
     If COSMOSObject Is Nothing Then ErrorMsg SwApp, "COSMOSObject object not found", True
    Set COSMOSWORKS = COSMOSObject.COSMOSWORKS
     If COSMOSWORKS Is Nothing Then ErrorMsg SwApp, "COSMOSWORKS object not found", True
   'Open the active document and use the COSMOSWORKS API
```

...

```vb
End Sub
```

###### VB.NET

Partial Class SolidWorksMacro
Public Sub main()

Dim COSMOSWORKS As Object
Dim COSMOSObject As Object
Dim swVersion As Integer
Dim cwVersion As Integer
Dim cwProgID As String

...

'Determine host SOLIDWORKS major version
swVersion = Convert.ToInt32(swApp.**RevisionNumber**().Substring(0, 2))

'Calculate the version-specific ProgID of the Simulation add-in that is compatible with this version of SOLIDWORKS
cwVersion = swVersion - 15
cwProgID = String.Format("SldWorks.Simulation.{0}", cwVersion)
Debug.Print(cwProgID)

'Get the SOLIDWORKS Simulation object
COSMOSObject = swApp.**GetAddInObject**(cwProgID)
If COSMOSObject Is Nothing Then ErrorMsg(swApp, "COSMOSObject object not found", True)
COSMOSWORKS = COSMOSObject.**CosmosWorks**
If COSMOSWORKS Is Nothing Then ErrorMsg(swApp, "COSMOSWORKS object not found", True)

'Open the active document and use the COSMOSWORKS API

...

End Sub

''' <summary>
''' The SldWorks swApp variable is pre-assigned for you.
''' </summary>
Public swApp As SldWorks
End Class

###### C#

partial class SolidWorksMacro
{
public void Main()
{
dynamic COSMOSWORKS = default(dynamic);
dynamic COSMOSObject = default(dynamic);

...

// Determine host SOLIDWORKS major version
int swVersion = Convert.ToInt32(swApp.**RevisionNumber**().Substring(0, 2));

// Calculate the version-specific ProgID of the Simulation add-in that is compatible with this version of SOLIDWORKS
int cwVersion = swVersion - 15;
String cwProgID = String.Format("SldWorks.Simulation.{0}", cwVersion);
Debug.Print(cwProgID);

// Get the SOLIDWORKS Simulation object
COSMOSObject = swApp.**GetAddInObject**(cwProgID);
if (COSMOSObject == null) ErrorMsg(swApp, "COSMOSObject object not found", true);
COSMOSWORKS = COSMOSObject.**CosmosWorks**;
if (COSMOSWORKS == null) ErrorMsg(swApp, "COSMOSWORKS object not found", true);

// Open the active document and use the COSMOSWORKS API

...

}

/// <summary>
/// The SldWorks swApp variable is pre-assigned for you.
/// </summary>
public SldWorks swApp;
}

###### Unmanaged C++ COM

```vb
 #include "stdafx.h"
 #include <string>
 #import "sldworks.tlb" raw_interfaces_only, raw_native_types, no_namespace, named_guids  // SOLIDWORKS type library
 #import "swconst.tlb" raw_interfaces_only, raw_native_types, no_namespace, named_guids   // SOLIDWORKS constants type library
 #import "cosworks.tlb" raw_interfaces_only, raw_native_types, no_namespace, named_guids   // SOLIDWORKS Simulation type library

 using namespace std;

 int _tmain(int argc, _TCHAR* argv[])
{

    // Initialize COM
     // Do this before using ATL smart pointers so that
     // COM is available
    CoInitialize(NULL);

     // Use a block so that the smart pointers are destructed when
     // the scope of this block is exited
    {
        // Use ATL smart pointers
         CComPtr<ISldWorks>  pSwApp;
         CComPtr<ICosmosWorks> pCOSMOSWORKS;
         CComPtr<IDispatch> pCOSMOSDispatch;
         CComPtr<ICwAddincallback> pCOSMOSObject;
         CComPtr<IDispatch> pDispatchSafeArray = NULL;
         CComPtr<ISafeArrayUtility> pSwSafeArray = NULL;
         HRESULT hres;

         if (pSwApp.CoCreateInstance(__uuidof(SldWorks), NULL, CLSCTX_LOCAL_SERVER) != S_OK) {
             return(0);
        }
        if (pSwApp.CoCreateInstance(__uuidof(ICosmosWorks), NULL, CLSCTX_LOCAL_SERVER) != S_OK) {
             return(0);
        }
        if (pSwApp.CoCreateInstance(__uuidof(IDispatch), NULL, CLSCTX_LOCAL_SERVER) != S_OK) {
             return(0);
        }
        if (pSwApp.CoCreateInstance(__uuidof(ICwAddincallback), NULL, CLSCTX_LOCAL_SERVER) != S_OK) {
             return(0);
        }
        hres = pSwApp->GetSafeArrayUtility(&pDispatchSafeArray);
        hres = pDispatchSafeArray.QueryInterface<ISafeArrayUtility>(&pSwSafeArray);

         // Determine host SOLIDWORKS major version
         USES_CONVERSION;
         CComBSTR bstrNum;
        std::string strNum;
         char *buffer;

        pSwApp->RevisionNumber(&bstrNum);
        strNum = W2A(bstrNum);
         long m_swMajNum = strtol(strNum.c_str(), &buffer, 10);

         // Calculate the version-specific ProgID of the Simulation add-in that is compatible with this version of SOLIDWORKS
         long cwVersion;
        cwVersion = m_swMajNum - 15;
         CComBSTR cwProgID;
         CComBSTR strVersion;
         wchar_t temp_str[11];
        _itow_s(cwVersion, temp_str, 10);
        strVersion = SysAllocString(temp_str);
        cwProgID = OLESTR("SldWorks.Simulation.");
        strVersion = cwProgID.Append(strVersion);

         // Get the SOLIDWORKS Simulation object
        pSwApp->GetAddInObject(strVersion, &pCOSMOSDispatch);

        if (pCOSMOSDispatch == NULL) {
             CComBSTR msg;
            msg = (OLESTR("COSMOSObject object not found: "));
             long res;
            pSwApp->SendMsgToUser2(msg, 0, 0, &res);
        }

        hres = pCOSMOSDispatch->QueryInterface(__uuidof(CwAddincallback),(void**)&pCOSMOSObject);
        pCOSMOSObject->get_CosmosWorks(&pCOSMOSWORKS);

        if (pCOSMOSWORKS == NULL) {
             CComBSTR msg;
            msg = (OLESTR("COSMOSWORKS object not found: "));
             long res;
            pSwApp->SendMsgToUser2(msg, 0, 0, &res);
        }

        // Open the active document and use the COSMOSWORKS API
        . . .

     }
     // ATL smart pointers are destructed so that all COM objects
     // held on to are released
      // Shut down COM because you no longer need it

     // Stop COM
     CoUninitialize();

     return(0);
 }
```

See [Accessing SOLIDWORKS Objects](Accessing_Objects.htm).
