
from django.urls import path
from . import views

# # MWANZO IN ORDER TO USE MODEL VIEW SET
from rest_framework.routers import DefaultRouter

router = DefaultRouter()


router.register('PostMyUser', views.MyUserViewSet)



router.register('PostHotelInventory', views.HotelInventoryViewSet)
router.register('PostHotelFoodCategories', views.HotelFoodCategoriesViewSet)
router.register('PostHotelDrinksCategories', views.HotelDrinksCategoriesViewSet)
router.register('PostRoomsClasses', views.RoomsClassesViewSet)
router.register('PostHotelCustomers', views.HotelCustomersViewSet)




# HOTEL FOOD PRODUCT
router.register('PostHotelOtherFoodProducts', views.HotelOtherFoodProductsViewSet)
router.register('PostHotelPizzaProducts', views.HotelPizzaProductsViewSet)


# HOTEL DRINKS PRODUCT
router.register('PostHotelSoftDrinksProducts', views.HotelSoftDrinksProductsViewSet)
router.register('PostHotelBeersProducts', views.HotelBeersProductsViewSet)



#--------------UNORDERED HOTEL ROOMS-----------------
router.register('PostHotelRoomsClassA', views.HotelRoomsClassAViewSet)
router.register('PostHotelRoomsClassB', views.HotelRoomsClassBViewSet)
router.register('PostHotelRoomsClassC', views.HotelRoomsClassCViewSet)
router.register('PostHotelRoomsClassD', views.HotelRoomsClassDViewSet)
router.register('PostHotelRoomsClassE', views.HotelRoomsClassEViewSet)



#--------------BOOKED HOTEL ROOMS-----------------
router.register('PostHotelBookedRoomsClassA', views.HotelBookedRoomsClassAViewSet)
router.register('PostHotelBookedRoomsClassB', views.HotelBookedRoomsClassBViewSet)
router.register('PostHotelBookedRoomsClassC', views.HotelBookedRoomsClassCViewSet)
router.register('PostHotelBookedRoomsClassD', views.HotelBookedRoomsClassDViewSet)
router.register('PostHotelBookedRoomsClassE', views.HotelBookedRoomsClassEViewSet)











#-----------------------RESTAURANT----------------------


router.register('PostRestaurantInventory', views.RestaurantInventoryViewSet)
router.register('PostRestaurantFoodCategories', views.RestaurantFoodCategoriesViewSet)
router.register('PostRestaurantDrinksCategories', views.RestaurantDrinksCategoriesViewSet)

router.register('PostRestaurantCustomers', views.RestaurantCustomersViewSet)






# HOTEL FOOD PRODUCT
router.register('PostRestaurantOtherFoodProducts', views.RestaurantOtherFoodProductsViewSet)
router.register('PostRestaurantPizzaProducts', views.RestaurantPizzaProductsViewSet)


# Restaurant DRINKS PRODUCT
router.register('PostRestaurantSoftDrinksProducts', views.RestaurantSoftDrinksProductsViewSet)
router.register('PostRestaurantBeersProducts', views.RestaurantBeersProductsViewSet)












#-----------------------RETAILS-------------------------




router.register('PostRetailsInventory', views.RetailsInventoryViewSet)
router.register('PostRetailsFoodCategories', views.RetailsFoodCategoriesViewSet)
router.register('PostRetailsDrinksCategories', views.RetailsDrinksCategoriesViewSet)

router.register('PostRetailsCustomers', views.RetailsCustomersViewSet)












# HOTEL FOOD PRODUCT
router.register('PostRetailsOtherFoodProducts', views.RetailsOtherFoodProductsViewSet)
router.register('PostRetailsPizzaProducts', views.RetailsPizzaProductsViewSet)


# Retails DRINKS PRODUCT
router.register('PostRetailsSoftDrinksProducts', views.RetailsSoftDrinksProductsViewSet)
router.register('PostRetailsBeersProducts', views.RetailsBeersProductsViewSet)




urlpatterns = router.urls