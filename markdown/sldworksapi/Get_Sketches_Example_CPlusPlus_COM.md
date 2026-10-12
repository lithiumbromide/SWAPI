---
title: "Get Sketches Example (C++ COM)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Sketches_Example_CPlusPlus_COM.htm"
---

# Get Sketches Example (C++ COM)

If you use a sketch to create a feature on your solid body, that sketch is a subfeature of that solid feature. This is illustrated by expanding and examining the FeatureManager design tree of a SOLIDWORKS Design feature.

This example shows how to traverse the FeatureManager design tree and use subfeature traversal to grab the ISketch objects used by each feature.

```vb
// Precompiled header
#include "stdafx.h"
#include <mbstring.h>

// SOLIDWORKS includes
#include <amapp.h>

// User Dll includes
#include "userapp.h"

void GetSketchesCOM()
{

LPMODELDOC pModelDoc;
HRESULT hres = UserApp->getSWApp()->get_IActiveDoc( &pModelDoc );

LPFEATURE pFeature = NULL;

// Get first feature in document
hres = pModelDoc->IFirstFeature(&pFeature);
int count = 0;

// While features exist
while (pFeature)
{

BSTR bFeatName;
// Get the feature name
hres = pFeature->get_Name( &bFeatName );
CString featName( bFeatName );
CString message;
message.Format( _T("\n\nFeature: %s"), bFeatName);

LPFEATURE pSubFeat;

// Get the subfeature
hres = pFeature->IGetFirstSubFeature( &pSubFeat );

if (pSubFeat != NULL)
// Print to Debug Output Window
  TRACE1("%s",message);

// Popup dialog for Release builds
//  AfxMessageBox( message );

// While subfeatures exist
while ( pSubFeat )
{

BSTR bFeatureTypeName;

// Get the subfeature type
hres = pSubFeat->GetTypeName(&bFeatureTypeName);
CString featureTypeName(bFeatureTypeName);

// If the sub-feature is a Sketch
if (featureTypeName == "ProfileFeature")
{
LPUNKNOWN iUnk = NULL;

// Get the Sketch interface
hres = pSubFeat->IGetSpecificFeature( &iUnk );

LPSKETCH pSketch;
hres = iUnk->QueryInterface( IID_ISketch, (LPVOID*)&pSketch);

if ( (hres == S_OK) && (pSketch != NULL) )
{
BSTR bSubFeatName;

// Get the sub-feature name
hres = pSubFeat->get_Name( &bSubFeatName );
CString subFeatName( bSubFeatName );
CString message;
message.Format( _T("\n\tSketch:\t%s\n"), bSubFeatName );

// Print to Debug Output Window
TRACE1("%s",message);

// Popup dialog for Release builds
// AfxMessageBox( message );

// Now that you have the Sketch used by this feature (pFeature) and
// you have its name, you can Select the sketch by calling
// SelectByID and passing the sketch name, or you can use the
// m_Sketch object to call the methods and properties available
// with the Sketch class.

// < YOUR CODE >

pSketch->Release();
}

// End if subfeature is a sketch
}

LPFEATURE pNextSubFeature;

// Get next subfeature
hres = pSubFeat->IGetNextSubFeature( & pNextSubFeature);
pSubFeat->Release();
pSubFeat = pNextSubFeature;

// End while subfeatures exist
}

LPFEATURE pNextFeature;

// Get next feature
hres = pFeature->IGetNextFeature(&pNextFeature);
pFeature->Release();
pFeature = pNextFeature;

// End while features exist
}

pModelDoc->Release();

// End function
}
```
